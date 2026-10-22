#!/usr/bin/env python3
"""Offline smoke tests for the resource discovery parser."""
import unittest

from discover_resources import candidate_priority, classify, validate_content


class ClassifyTests(unittest.TestCase):
    def test_tvbox_json(self):
        self.assertEqual(classify("dist/official.json"), "json")
        self.assertEqual(classify("config/sources.json"), "json")

    def test_m3u(self):
        self.assertEqual(classify("live.m3u"), "m3u")
        self.assertEqual(classify("folder/playlist.m3u8"), "m3u")

    def test_unrelated_text_is_ignored(self):
        self.assertIsNone(classify("docs/tutorial.txt"))

    def test_build_metadata_is_ignored(self):
        self.assertIsNone(classify("package-lock.json"))
        self.assertIsNone(classify(".claude/settings.json"))
        self.assertIsNone(classify("output/status.json"))

    def test_client_configs_rank_first(self):
        self.assertLess(candidate_priority("tvbox.json"), candidate_priority("json/123.json"))
        self.assertLess(candidate_priority("dist/official.json"), candidate_priority("package.json"))


class ValidationTests(unittest.TestCase):
    def test_tvbox_json(self):
        status, _, count = validate_content("json", b'{"sites":[{"key":"demo"}]}')
        self.assertEqual(status, "tvbox-config")
        self.assertEqual(count, 1)

    def test_valid_non_tvbox_json(self):
        status, _, _ = validate_content("json", b'{"hello":"world"}')
        self.assertEqual(status, "valid-json-other")

    def test_invalid_json(self):
        status, _, _ = validate_content("json", b'{"sites":}')
        self.assertEqual(status, "invalid-json")

    def test_m3u(self):
        status, _, count = validate_content("m3u", b'#EXTM3U\n#EXTINF:-1,Demo\nhttps://example.invalid/live.m3u8\n')
        self.assertEqual(status, "valid-m3u")
        self.assertEqual(count, 1)

    def test_bad_m3u(self):
        status, _, _ = validate_content("m3u", b'https://example.invalid')
        self.assertEqual(status, "invalid-m3u")


if __name__ == "__main__":
    unittest.main()
