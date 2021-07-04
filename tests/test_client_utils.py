""" Test Client Utils
"""

import unittest
from .dtos import *
from servicestack import json_encode, qsvalue, resolve_httpmethod

class ClientUtils(unittest.TestCase):

    def test_json_encode(self):
        h = Hello(name='A')
        self.assertEqual(json_encode(None), 'null')
        self.assertEqual(json_encode("A"), '"A"')
        self.assertEqual(json_encode(1), '1')
        self.assertEqual(json_encode(h), '{"name": "A"}')
        self.assertEqual(json_encode([h,h]), '[{"name": "A"}, {"name": "A"}]')
        self.assertEqual(json_encode({'a':h,'b':h}), '{"a": {"name": "A"}, "b": {"name": "A"}}')

    def test_qsvalue(self):
        self.assertEqual(qsvalue(None), "")
        self.assertEqual(qsvalue("A"), "A")
        self.assertEqual(qsvalue(1), "1")
        self.assertEqual(qsvalue(b"Python"), "UHl0aG9u")

    def test_does_resolve_IVerbs_from_request_DTO_interface_marker(self):
        self.assertEqual(resolve_httpmethod(SendGet()), "GET")
        self.assertEqual(resolve_httpmethod(SendPost()), "POST")
        self.assertEqual(resolve_httpmethod(SendPut()), "PUT")
