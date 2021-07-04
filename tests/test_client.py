""" Basic Serialization Tests
"""

from requests.api import put
from servicestack.servicestack import json_encode
import unittest
from .dtos import *

from servicestack import JsonServiceClient

# TEST_URL = "https://localhost:5001"
TEST_URL = "http://localhost:5000"
def create_test_client():
    return JsonServiceClient(TEST_URL)

client = create_test_client()

class TestApi(unittest.TestCase):

    def test_can_get_hello(self):
        response:HelloResponse = client.get(Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_hello(self):
        response:HelloResponse = client.post(Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_send_umlauts(self):
        response:HelloResponse = client.post(Hello(name="üöäß"))
        self.assertEqual(response.result, "Hello, üöäß!")

    def test_does_fire_Request_and_Response_filters(self):
        client = create_test_client()
        events = []

        JsonServiceClient.global_request_filter = lambda info: events.append("globalRequestFilter")
        JsonServiceClient.global_response_filter = lambda res: events.append("globalResponseFilter")

        client.request_filter = lambda info: events.append("requestFilter")
        client.response_filter = lambda res: events.append("responseFilter")

        response:HelloResponse = client.get(Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")
        
        self.assertListEqual(events, [
          "requestFilter",
          "globalRequestFilter",
          "responseFilter",
          "globalResponseFilter"
        ])

        JsonServiceClient.global_request_filter = None
        JsonServiceClient.global_response_filter = None

    def test_can_get_hello_with_custom_path(self):
        response:HelloResponse = client.get_url("/hello/World", response_as=HelloResponse)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_get_hello_with_CustomPath_as_raw_types(self):
        json_str = client.get_url("/hello", response_as=str, args={'name':'World'})
        self.assertEqual(json_str, '{"result":"Hello, World!"}')

        json_bytes:bytes = client.get_url("/hello", response_as=bytes, args={'name':'World'})
        self.assertEqual(json_bytes.decode("utf-8"), '{"result":"Hello, World!"}')

        dto:HelloResponse = client.get_url("/hello", response_as=HelloResponse, args={'name':'World'})
        self.assertEqual(dto.result, "Hello, World!")

    def test_can_post_Hello_with_CustomPath(self):
        response:HelloResponse = client.post_url("/hello", Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_hello_with_CustomPath_json_object(self):
        json_obj = client.post_url("/hello", json_encode(Hello(name="World")))
        self.assertIsInstance(json_obj, dict)
        response = HelloResponse(**json_obj)
        self.assertEqual(response.result, "Hello, World!")
