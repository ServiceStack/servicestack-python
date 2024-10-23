""" Test Client Utils
"""

import unittest
import re
from .dtos import *
from servicestack import to_json, qsvalue, resolve_httpmethod


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLocationsResponse:
    locations: Optional[List[str]] = None


# @Route("/locations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLocations(IReturn[GetLocationsResponse], IGet):
    pass


def sanitize_html(s: str): return re.sub(r"\s", "", s)


class ClientUtils(unittest.TestCase):

    def test_json_encode(self):
        h = Hello(name='A')
        self.assertEqual(to_json(None), 'null')
        self.assertEqual(to_json("A"), '"A"')
        self.assertEqual(to_json(1), '1')
        self.assertEqual(to_json(h), '{"name": "A"}')
        self.assertEqual(to_json([h, h]), '[{"name": "A"}, {"name": "A"}]')
        self.assertEqual(to_json({'a': h, 'b': h}), '{"a": {"name": "A"}, "b": {"name": "A"}}')

    def test_qsvalue(self):
        self.assertEqual(qsvalue(None), "")
        self.assertEqual(qsvalue("A"), "A")
        self.assertEqual(qsvalue(1), "1")
        self.assertEqual(qsvalue(b"Python"), "UHl0aG9u")

    def test_does_resolve_IVerbs_from_request_DTO_interface_marker(self):
        self.assertEqual(resolve_httpmethod(SendGet()), "GET")
        self.assertEqual(resolve_httpmethod(SendPost()), "POST")
        self.assertEqual(resolve_httpmethod(SendPut()), "PUT")
        self.assertEqual(resolve_httpmethod(GetLocations()), "GET")

    def test_can_htmldump_different_types(self):
        self.assertEqual(htmldump(1), "1")
        self.assertEqual(htmldump("A"), "A")
        self.assertEqual(htmldump({"A": 1, "B": 2}),
                         "<table><tbody><tr><th>A</th><td>1</td></tr><tr><th>B</th><td>2</td></tr></tbody></table>")
        self.assertEqual(sanitize_html(htmldump(["A", 1])),
                         "<table><tbody><tr><td>A</td></tr><tr><td>1</td></tr></tbody></table>")
        self.assertEqual(sanitize_html(htmldump([{"A": 1, "B": 2}, {"A": 3, "B": 4}])),
                         "<table><thead><tr><th>A</th><th>B</th></tr></head><tbody><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></tbody></table>")
    
    # covid-vac-watch.netcore.io is down
    # def test_can_send_GetLocations(self):
    #     client = JsonServiceClient("https://covid-vac-watch.netcore.io")
    #     response = client.send(GetLocations())
    #     printdump(response)
    #     printhtmldump(response.locations)
