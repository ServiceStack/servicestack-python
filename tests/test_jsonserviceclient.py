"""JsonServiceClient Tests
"""
import unittest

from servicestack.clients import append_querystring
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
        request = EchoTypes(date_time=datetime.datetime(2015, 1, 1, tzinfo=datetime.timezone.utc))
        response: EchoTypes = client.get(request)
        self.assertEqual(response.date_time, request.date_time)

    def test_should_generate_default_value(self):
        client = create_test_client()
        request = HelloTypes(bool_=False, int_=0)
        request_url = append_querystring(TEST_URL, to_dict(request, key_case=clean_camelcase))
        self.assertEqual(request_url, TEST_URL + "?bool=false&int=0")
