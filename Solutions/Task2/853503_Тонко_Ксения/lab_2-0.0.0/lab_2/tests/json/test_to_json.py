import unittest
import lab_2.tasks.json.json_converter as js
import json


class TestToJson(unittest.TestCase):

    def test_int(self):
        result = js.JsonConverter.to_json(157)
        self.assertEqual(result, json.dumps(157))

    def test_float(self):
        result = js.JsonConverter.to_json(-69.345105)
        self.assertEqual(result, json.dumps(-69.345105))

    def test_bool(self):
        result = js.JsonConverter.to_json(True)
        self.assertEqual(result, json.dumps(True))
        result = js.JsonConverter.to_json(False)
        self.assertEqual(result, json.dumps(False))

    def test_none(self):
        result = js.JsonConverter.to_json(None)
        self.assertEqual(result, json.dumps(None))

    def test_str(self):
        result = js.JsonConverter.to_json("gjag\\ae74r\"srxgfn")
        self.assertEqual(result, json.dumps("gjag\\ae74r\"srxgfn"))

    def test_tuple(self):
        tup = (2, -3, 5, ("qwer", (True, (None, False, (12, 5)))), "a")
        result = js.JsonConverter.to_json(tup)
        self.assertEqual(result, json.dumps(tup))

    def test_list(self):
        lst = ["asd", (2, "sf"), 5741, True, [5, -749.52, ["QWe", "st", 74.15], None]]
        result = js.JsonConverter.to_json(lst)
        self.assertEqual(result, json.dumps(lst))

    def test_dict(self):
        dct = {1: (13, 7), 55: {14: 7}, "qw": False, True: {"y": {-58: [5.2, None, True], 3: 2}}, 6: (2, 3)}
        result = js.JsonConverter.to_json(dct)
        self.assertEqual(result, json.dumps(dct))
