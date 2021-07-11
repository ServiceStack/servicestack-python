"""JsonServiceClient Tests
"""
import operator
import unittest
from dataclasses_json import dataclass_json, LetterCase, Undefined, config
import dataclasses

import requests
from dataclasses_json import config, dataclass_json, Undefined

from servicestack.utils import *
from tests.config import *
from .dtos import *


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NonExistingService(IReturn[str]):
    data: Optional[str] = None


class TestJsonServiceClient(unittest.TestCase):

    def test_does_process_missing_service_correctly(self):
        client = create_test_client()
        try:
            client.get(NonExistingService())
        except WebServiceException as e:
            self.assertEqual(e.status_code, 405)

    def test_does_serialize_dates_correctly_via_get_request(self):
        client = create_test_client()
        request = EchoTypes(date_time=datetime.datetime(2015, 1, 1, tzinfo=timezone.utc))
        response: EchoTypes = client.get(request)
        self.assertEqual(response.date_time, request.date_time)
