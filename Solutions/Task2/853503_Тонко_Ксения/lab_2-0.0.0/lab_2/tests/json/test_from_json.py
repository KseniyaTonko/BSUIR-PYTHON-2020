import unittest
import lab_2.tasks.json.json_converter as js
import json


class TestFromJson(unittest.TestCase):

    def test_int(self):
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(-78462))
        self.assertEqual(result, json.loads(json.dumps(-78462)))

    def test_float(self):
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(58.123456))
        self.assertEqual(result, json.loads(json.dumps(58.123456)))

    def test_bool(self):
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(True))
        self.assertEqual(result, json.loads(json.dumps(True)))

    def test_none(self):
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(None))
        self.assertEqual(result, json.loads(json.dumps(None)))

    def test_str(self):
        result = js.JsonConverter.from_json(js.JsonConverter.to_json("esrg\\seg74923$@\"78"))
        self.assertEqual(result, json.loads(json.dumps("esrg\\seg74923$@\"78")))

    def test_tuple(self):
        tpl = (2, 8.2, "asdF", None, True, (5, 66, False), "szgdgz")
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(tpl))
        self.assertEqual(result, json.loads(json.dumps(tpl)))

    def test_list(self):
        lst = ["asd", 5741, True, [5, 7, 87, 749.52, ["QWe", "st", 74.15], None], (2, 3)]
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(lst))
        self.assertEqual(result, json.loads(json.dumps(lst)))

    def test_dict(self):
        dct = {1: 13, 2: 48, 55: {14: 7}, "qwrszf": False, True: {"y": {58: [5.2, None, True], 3: 2}}, "G": "ade"}
        result = js.JsonConverter.from_json(js.JsonConverter.to_json(dct))
        self.assertEqual(result, json.loads(json.dumps(dct)))
