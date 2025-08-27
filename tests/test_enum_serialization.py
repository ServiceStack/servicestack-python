"""Enum Serialization
"""

import unittest
import json

from servicestack import to_json, convert
from servicestack.utils import *
from tests.dtos import HelloWithEnum
from .dtos import *


class TestEnumSerialization(unittest.TestCase):

    def assert_HelloWithEnum(self, actual: HelloWithEnum, expected: HelloWithEnum):
        self.assertEqual(actual.enum_prop, expected.enum_prop)
        self.assertEqual(actual.enum_with_values, expected.enum_with_values)
        self.assertEqual(actual.nullable_enum_prop, expected.nullable_enum_prop)
        self.assertEqual(actual.enum_flags, expected.enum_flags)
        self.assertEqual(actual.enum_style, expected.enum_style)

    def test_does_serialize_HelloWithEnum_empty(self):
        dto = HelloWithEnum()
        json_str = to_json(dto)
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnum, json_obj)
        self.assertEqual(from_json_obj, dto)

    def test_does_serialize_HelloWithEnum_EnumFlags(self):
        dto = HelloWithEnum(enum_flags=EnumFlags.VALUE1)
        json_str = to_json(dto)
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnum, json_obj)
        self.assertEqual(from_json_obj, dto)

    def test_does_serialize_HelloWithEnum_all(self):
        dto = HelloWithEnum(
            enum_prop=EnumType.VALUE2,
            enum_with_values=EnumWithValues.VALUE1,
            enum_flags=EnumFlags.VALUE1,
            enum_style=EnumStyle.UPPER)
        json_str = to_json(dto)
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnum, json_obj)
        self.assertEqual(from_json_obj, dto)

    def assert_HelloWithEnumMap(self, actual: HelloWithEnumMap, expected: HelloWithEnumMap):
        self.assertDictEqual(actual.enum_prop, expected.enum_prop)
        self.assertDictEqual(actual.enum_with_values, expected.enum_with_values)
        self.assertDictEqual(actual.nullable_enum_prop, expected.nullable_enum_prop)
        self.assertDictEqual(actual.enum_flags, expected.enum_flags)
        self.assertDictEqual(actual.enum_style, expected.enum_style)

    def test_does_serialize_HelloWithEnumMap_empty(self):
        dto = HelloWithEnumMap()
        json_str = to_json(dto)
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnumMap, json_obj)
        self.assertEqual(from_json_obj, dto)

    def test_does_serialize_HelloWithEnumMap_all(self):
        dto = HelloWithEnumMap(
            enum_prop={f"{EnumType.VALUE2}": EnumType.VALUE2},
            enum_with_values={f"{EnumWithValues.VALUE1}": EnumWithValues.VALUE1},
            enum_flags={f"{EnumFlags.VALUE1}": EnumFlags.VALUE1},
            enum_style={f"{EnumStyle.UPPER}": EnumStyle.UPPER})
        json_str = to_json(dto)
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnumMap, json_obj)
        self.assertEqual(from_json_obj, dto)

    def test_does_serialize_list_of_enums_on_queryString(self):
        dto = HelloWithEnumList(
            enum_flags=[EnumFlags.VALUE1, EnumFlags.VALUE2],
            enum_style=[EnumStyle.LOWER, EnumStyle.UPPER])
        json_str = to_json(dto)

        print("HelloWithEnumList")
        print(json.dumps(json.loads(json_str), indent=2))
        json_obj = json.loads(json_str)
        from_json_obj = convert(HelloWithEnumList, json_obj)
        self.assertEqual(from_json_obj, dto)
        self.assertEqual(qsvalue(dto.enum_flags), "[1,2]")
        self.assertEqual(qsvalue(dto.enum_style), "[lower,UPPER]")
