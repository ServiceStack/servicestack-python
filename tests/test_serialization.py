"""Serialization Tests
"""
import unittest

import io
import json
import datetime
from servicestack.clients import append_querystring, UploadFile
from servicestack.utils import *
from servicestack.reflection import _json_encoder, to_dict, to_jsv_data
from tests.config import *
from .dtos import *
from tests.test_client import create_AllTypes, create_AllCollectionTypes, \
    assert_AllTypes, assert_AllCollectionTypes

JSON_ALL_TYPES = '{"id":1,"byte":2,"short":3,"int":4,"long":5,"uShort":6,"uInt":7,"uLong":8,"float":1.1,"double":2.2,"decimal":3.0,"string":"string","dateTime":"\/Date(978307200000)\/","timeSpan":"PT1H","dateTimeOffset":"\/Date(978307200000)\/","guid":"ea762009b66c410b9bf5ce21ad519249","char":"c","keyValuePair":{},"stringList":["A","B","C"],"stringArray":["D","E","F"],"stringMap":{"A":"D","B":"E","C":"F"},"intStringMap":{"1":"A","2":"B","3":"C"},"subType":{"id":1,"name":"name"}}'
JSON_ALL_COLLECTION_TYPES = '{"intArray":[1,2,3],"intList":[4,5,6],"stringArray":["A","B","C"],"stringList":["D","E","F"],byteArray:"QUJD","pocoArray":[{"name":"pocoArray"}],"pocoList":[{"name":"pocoList"}],"pocoLookup":{"A":[{"name":"B"},{"name":"C"}]},"pocoLookupMap":{"A":[{"B":{"name":"C"}},{"D":{"name":"E"}}]}}'

@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestUpload(IReturn["TestUpload"], IPost):
    int_: int = field(metadata=config(field_name='int'), default=0)
    nullable_id: Optional[int] = None
    long: int = 0
    double: float = 0.0
    string: Optional[str] = None
    date_time: datetime.datetime = datetime.datetime(1, 1, 1)
    int_array: List[int] = field(default_factory=list)
    int_list: List[int] = field(default_factory=list)
    string_array: List[str] = field(default_factory=list)
    string_list: List[str] = field(default_factory=list)
    poco_array: List[Poco] = field(default_factory=list)
    poco_list: List[Poco] = field(default_factory=list)
    nullable_byte_array: List[Optional[int]] = field(default_factory=list)
    nullable_byte_list: List[int] = field(default_factory=list)
    nullable_date_time_array: List[Optional[datetime.datetime]] = field(default_factory=list)
    nullable_date_time_list: List[datetime.datetime] = field(default_factory=list)
    poco_lookup: Dict[str, List[Poco]] = field(default_factory=dict)
    poco_lookup_map: Dict[str, List[Dict[str, Poco]]] = field(default_factory=dict)
    map_list: Optional[Dict[str, List[str]]] = None

class TestSerialization(unittest.TestCase):

    def test_does_serialize_AllTypes(self):
        dto = create_AllTypes()
        json_str = to_json(dto)
        json_obj = from_json(AllTypes, json_str)
        assert_AllTypes(self, json_obj)

    def test_does_deserialize_AllTypes(self):
        json_obj = from_json(AllTypes, JSON_ALL_TYPES)
        assert_AllTypes(self, json_obj)

    def test_does_serialize_AllCollectionTypes(self):
        dto = create_AllCollectionTypes()
        json_str = to_json(dto)
        json_obj = from_json(AllCollectionTypes, json_str)
        assert_AllCollectionTypes(self, json_obj)

    def test_does_serialize_HelloAllTypes(self):
        dto = HelloAllTypes(
            name="HelloAllTypes",
            all_types=create_AllTypes(),
            all_collection_types=create_AllCollectionTypes())
        json_str = to_json(dto)
        json_obj: HelloAllTypes = from_json(HelloAllTypes, json_str)
        self.assertEqual(dto.name, json_obj.name)
        assert_AllTypes(self, json_obj.all_types)
        assert_AllCollectionTypes(self, json_obj.all_collection_types)

    def test_does_serialize_inheritance(self):
        dto = HelloWithInheritance(name="foo", id=1)
        json_str = to_json(dto)
        json_obj: HelloWithInheritance = from_json(HelloWithInheritance, json_str)
        self.assertEqual(json_obj.name, "foo")
        self.assertEqual(json_obj.id, 1)
