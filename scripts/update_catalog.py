#!/usr/bin/env python3
"""Discover GitHub TVBox JSON candidates. Never execute third-party code."""
import base64, ipaddress, json, os, re, socket, subprocess, time
import urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
README=ROOT/"README.md"; OUT=ROOT/"sources/catalog.json"; TESTS=ROOT/"sources/authorized-playback-tests.json"
TOKEN=os.getenv("GITHUB_TOKEN",""); SELF=os.getenv("GITHUB_REPOSITORY","passionsu-su/TVbox")
NOW=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
START="<!-- TVBOX-CATALOG:START -->"; END="<!-- TVBOX-CATALOG:END -->"
LICENSES={"MIT","Apache-2.0","BSD-2-Clause","BSD-3-Clause","MPL-2.0","GPL-2.0","GPL-3.0","LGPL-2.1","LGPL-3.0","CC0-1.0","Unlicense"}
QUERIES=['TVBox in:name,description','"影视仓" TVBox in:name,description','TVBox config JSON in:description']

def get(url, limit=1500000, github=False, redirects=True):
    h={"User-Agent":"TVbox-catalog-validator/1.0","Accept":"application/vnd.github+json" if github else "application/json,*/*"}
    if github and TOKEN: h["Authorization"]="Bearer "+TOKEN
    req=urllib.request.Request(url,headers=h)
    if not redirects:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self,req,fp,code,msg,headers,newurl):
                raise urllib.error.HTTPError(req.full_url,code,"redirect not followed",headers,fp)
        opener=urllib.request.build_opener(NoRedirect)
    else: opener=urllib.request.build_opener()
    with opener.open(req,timeout=12) as r:
        data=r.read(limit+1)
        if len(data)>limit: raise ValueError("response too large")
        return r.status,r.headers.get("Content-Type",""),data

def api(url): return json.loads(get(url,github=True)[2].decode())

def safe_url(url):
    try:
        p=urllib.parse.urlparse(url)
        if p.scheme not in ("http","https") or not p.hostname or p.username or p.password: return False,"invalid HTTP(S) URL"
        host=p.hostname.lower()
        if host=="localhost" or host.endswith((".local",".internal")): return False,"local hostname blocked"
        ips={x[4][0].split("%")[0] for x in socket.getaddrinfo(host,p.port or (443 if p.scheme=="https" else 80))}
        if not ips or any(not ipaddress.ip_address(x).is_global for x in ips): return False,"non-public IP blocked"
        return True,""
    except Exception as e: return False,str(e)[:120]

def safe_get(url,limit=1500000):
    ok,why=safe_url(url)
    if not ok: raise ValueError(why)
    return get(url,limit=limit,redirects=False)

def extract(text):
    out=set()
    for u in re.findall(r'https?://[^\s\)\]\}"<>]+',text):
        u=u.rstrip(".,;"); p=urllib.parse.urlparse(u)
        if p.hostname not in ("github.com","raw.githubusercontent.com") or not p.path.lower().endswith(".json"): continue
        if p.hostname=="github.com":
            m=re.match(r"^/([^/]+)/([^/]+)/blob/([^/]+)/(.+\.json)$",p.path)
            if not m: continue
            a,b,c,d=m.groups(); u=f"https://raw.githubusercontent.com/{a}/{b}/{c}/{d}"
        out.add(u)
    return sorted(out)

def validate(raw):
    try: o=json.loads(raw.decode("utf-8-sig"))
    except Exception as e: return False,"JSON parse error: "+str(e)[:100],None
    if not isinstance(o,dict): return False,"top-level must be object",None
    keys=set(o)&{"sites","lives","parses","spider","rules","ads"}
    if not keys: return False,"no known TVBox config keys",o
    if "sites" in o and not isinstance(o["sites"],list): return False,"sites must be array",o
    if any(not isinstance(x,dict) for x in o.get("sites",[]) if isinstance(o.get("sites",[]),list)): return False,"sites has non-object entry",o
    return True,"valid JSON; keys "+",".join(sorted(keys)),o

def endpoint(url):
    try:
        status,ct,data=safe_get(url,200000)
        return "接口可访问",f"HTTP {status}; {ct or 'unknown'}; {len(data)} bytes (not playback proof)"
    except urllib.error.HTTPError as e:
        return ("重定向未跟随" if e.code in (301,302,303,307,308) else "接口检测失败"),f"HTTP {e.code}"
    except Exception as e: return "接口检测失败",str(e)[:150]

def discover():
    found={}
    for q in QUERIES:
        try:
            u="https://api.github.com/search/repositories?"+urllib.parse.urlencode({"q":q,"sort":"stars","order":"desc","per_page":15})
            for r in api(u).get("items",[]):
                if r.get("full_name","").lower()!=SELF.lower(): found[r["full_name"]]=r
        except Exception as e: print("WARN search:",str(e)[:120])
        time.sleep(1)
    return sorted(found.values(),key=lambda x:x.get("stargazers_count",0),reverse=True)[:30]

def candidates(r):
    name=r["full_name"]; branch=r.get("default_branch") or "main"; out=set()
    try:
        rd=api(f"https://api.github.com/repos/{name}/readme")
        out.update(extract(base64.b64decode(rd.get("content","")).decode("utf-8","replace")))
    except Exception: pass
    try:
        tree=api(f"https://api.github.com/repos/{name}/git/trees/{urllib.parse.quote(branch,safe='')}?recursive=1")
        for item in tree.get("tree",[])[:4000]:
            path=item.get("path",""); low=path.lower()
            if item.get("type")=="blob" and low.endswith(".json") and item.get("size",0)<=1500000 and any(k in low for k in ("tvbox","config","source","api","site","jsm","box","wx")):
                out.add(f"https://raw.githubusercontent.com/{name}/{branch}/{urllib.parse.quote(path,safe='/')}")
            if len(out)>=8: break
    except Exception: pass
    return sorted(out)[:8]

def playback():
    try: tests=json.loads(TESTS.read_text(encoding="utf-8")).get("tests",[])
    except Exception: return []
    result=[]
    for t in tests:
        name=t.get("name","unnamed")
        if not t.get("authorization_evidence") or not t.get("media_url"):
            result.append({"name":name,"status":"未执行","detail":"missing authorization evidence or media URL","checked_at":NOW}); continue
        ok,why=safe_url(t["media_url"])
        if not ok:
            result.append({"name":name,"status":"检测失败","detail":why,"checked_at":NOW}); continue
        try:
            p=subprocess.run(["ffprobe","-v","error","-show_entries","stream=codec_type,codec_name","-of","json",t["media_url"]],capture_output=True,text=True,timeout=25)
            info=json.loads(p.stdout or "{}") if p.returncode==0 else {}
            has=any(s.get("codec_type") in ("audio","video") for s in info.get("streams",[]))
            if not has:
                result.append({"name":name,"status":"检测失败","detail":(p.stderr or "no audio/video stream")[-150:],"checked_at":NOW})
                continue
            # Decode a short sample instead of merely checking the HTTP response.
            decoded=subprocess.run(["ffmpeg","-v","error","-i",t["media_url"],"-t","5","-f","null","-"],capture_output=True,text=True,timeout=35)
            result.append({"name":name,"status":"媒体解码测试通过（非 TVBox 客户端）" if decoded.returncode==0 else "媒体解码失败","detail":"FFmpeg decoded up to 5 seconds; still not actual TVBox-client playback" if decoded.returncode==0 else (decoded.stderr or "ffmpeg decode failed")[-150:],"checked_at":NOW})
        except Exception as e: result.append({"name":name,"status":"检测失败","detail":str(e)[:150],"checked_at":NOW})
    return result

def esc(x): return str(x or "—").replace("|","\\|").replace("\n"," ")

def main():
    rows=[]; seen=set()
    for repo in discover():
        lic=(repo.get("license") or {}).get("spdx_id") or "NOASSERTION"
        for url in candidates(repo):
            if url in seen: continue
            seen.add(url)
            row={"url":url,"repository":repo["full_name"],"repository_url":repo.get("html_url","https://github.com/"+repo["full_name"]),"stars":repo.get("stargazers_count",0),"license":lic,"checked_at":NOW,"format_status":"未检测","interface_status":"未检测","playback_status":"未实播验证","notes":"","authorization_status":"仓库声明开放许可证；配置和媒体授权仍需人工核实" if lic in LICENSES else "许可证/授权待核实"}
            try:
                status,ct,raw=safe_get(url); ok,note,obj=validate(raw)
                row["format_status"]="格式通过" if ok else "格式失败"; row["notes"]=f"HTTP {status}; {note}"
                if ok:
                    apis=[s.get("api") for s in obj.get("sites",[])[:30] if isinstance(s,dict) and isinstance(s.get("api"),str) and s["api"].startswith(("http://","https://"))]
                    if apis:
                        row["interface_status"],detail=endpoint(apis[0]); row["notes"]+="; first API: "+detail
            except Exception as e: row["format_status"]="检测失败"; row["notes"]=str(e)[:180]
            rows.append(row)
        time.sleep(.25)
    rows.sort(key=lambda r:(r["format_status"]!="格式通过",r["interface_status"]!="接口可访问",-r["stars"],r["repository"]))
    tests=playback()
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({"generated_at":NOW,"count":len(rows),"entries":rows,"authorized_playback_tests":tests,"limitations":["HTTP success does not prove playback.","Repository license does not prove media rights.","No third-party scripts/JARs are executed.","ffprobe is not actual TVBox client playback."]},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=[START,"## 每周自动发现与检测结果","",f"> 最近检测：**{NOW}**。候选来自 GitHub 公开项目；结果不是安全审计、版权授权或客户端实播成功证明。仓库许可证不能证明配置指向的站点/媒体内容已获授权。","",f"- 候选 JSON：**{len(rows)}**","- 只读取 JSON，不下载或执行第三方 Spider/JAR/脚本。","- 格式通过不代表接口可用；接口可访问不代表可播放。授权未核实的条目仅作诊断候选。","","| 配置 JSON | 来源仓库 | Stars | 许可证 | JSON 检测 | API 检测 | 播放状态 | 授权说明 | 检测时间 / 备注 |","|---|---|---:|---|---|---|---|---|---|"]
    if not rows: lines.append("| 暂无候选 | — | — | — | — | — | 未实播验证 | — | 本周未发现可检查配置 |")
    for r in rows[:60]:
        lines.append(f"| [配置]({r['url']}) | [{esc(r['repository'])}]({r['repository_url']}) | {r['stars']} | {esc(r['license'])} | {esc(r['format_status'])} | {esc(r['interface_status'])} | {esc(r['playback_status'])} | {esc(r['authorization_status'])} | {esc(r['checked_at'])}；{esc(r['notes'])} |")
    lines += ["","### 经授权测试源的媒体流探测","","只有在 sources/authorized-playback-tests.json 中填写授权依据和直接媒体 URL 的条目才会执行 ffprobe；这仍不等于 TVBox 客户端实播。",""]
    if not tests: lines.append("当前未配置经授权的媒体测试源；本次没有任何资源被标记为已实播成功。")
    else:
        lines += ["| 测试源 | 结果 | 备注 | 检测时间 |","|---|---|---|---|"]
        for t in tests: lines.append(f"| {esc(t.get('name'))} | {esc(t.get('status'))} | {esc(t.get('detail'))} | {esc(t.get('checked_at'))} |")
    lines += ["","机器可读报告：[sources/catalog.json](sources/catalog.json)。","",END]
    section="\n".join(lines); readme=README.read_text(encoding="utf-8")
    if START in readme and END in readme: readme=readme.split(START,1)[0].rstrip()+"\n\n"+section+readme.split(END,1)[1]
    elif "## 本仓库怎么维护" in readme:
        a,b=readme.split("## 本仓库怎么维护",1); readme=a.rstrip()+"\n\n"+section+"\n\n## 本仓库怎么维护"+b
    else: readme=readme.rstrip()+"\n\n"+section+"\n"
    README.write_text(readme,encoding="utf-8")
    print(f"Wrote {len(rows)} candidate records")
if __name__=="__main__": main()
