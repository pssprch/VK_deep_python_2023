import unittest
from unittest.mock import Mock
from parse_json import parse_json

class TestParseJson(unittest.TestCase):

    def setUp(self):
        self.json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'

    def test_valid(self):
        func = Mock()
        parse_json(self.json_str, required_fields=["key1"], keywords=["word2"], keyword_callback=func)
        func.assert_called_once_with("key1", "word2")
    
    def test_invalid(self):
        invalid_json_str = '{"key1": word1"}'
        func = Mock()
        with self.assertLogs() as cm:
            parse_json(invalid_json_str, keyword_callback=func)
        self.assertIn("JSON Decode Error", cm.output[0])
        func.assert_not_called()

    def test_no_kw(self):
        func = Mock()
        parse_json(self.json_str, required_fields=["key1"], keywords=["word4"], keyword_callback=func)
        func.assert_not_called()

    def test_no_req(self):
        func = Mock()
        parse_json(self.json_str, keywords=["key1"], keyword_callback=func)
        func.assert_not_called()

    def test_case(self):
        func = Mock()
        parse_json(self.json_str, required_fields=["key2"], keywords=["WORD2"],keyword_callback=func)
        func.assert_called_once_with("key2", "WORD2")

    def test_empty(self):
        func = Mock()
        parse_json(" ", keyword_callback=func)
        func.assert_not_called()

    def test_not_cactused(self):
        func = Mock()
        json_str = '{"key": "cactused"}'
        parse_json(json_str, required_fields=["key"], keywords=["cactus"], keyword_callback=func)
        func.assert_not_called()

    def test_different_conditions_and_registers(self):
        func = Mock()
        json_str = '{"Key1": "Word1 word2", "KEY2": "word2 word3", "key3": "WoRd1 word2"}'

        parse_json(json_str, required_fields=["KEY2"], keywords=["word2"], keyword_callback=func)
        func.assert_called_once_with("KEY2", "word2")
        func.reset_mock()

        parse_json(json_str, required_fields=["key3"], keywords=["wOrD1"], keyword_callback=func)
        func.assert_called_once_with("key3", "wOrD1")
        func.reset_mock()


if __name__ == "__main__":
    unittest.main()
