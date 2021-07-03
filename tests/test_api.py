""" Basic Serialization Tests
"""

import unittest
import requests
import dataclasses
import operator
from .dtos import *

from servicestack import JsonServiceClient

from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json, Undefined
from typing import Optional

# TEST_URL = "https://localhost:5001"
TEST_URL = "http://localhost:5000"

class TestApi(unittest.TestCase):

    def test_does_dump(self):
        orgName = "python"
        client = JsonServiceClient(TEST_URL)
        response:HelloResponse = client.get(Hello(name="World"))
        print(response.result)
