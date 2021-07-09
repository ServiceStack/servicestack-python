""" Basic Serialization Tests
"""

from requests.api import put, request
import unittest
from .dtos import *
from datetime import datetime, timedelta, timezone

from servicestack import JsonServiceClient, WebServiceException, to_json

# TEST_URL = "https://localhost:5001"
TEST_URL = "http://localhost:5000"
def create_test_client():
    return JsonServiceClient(TEST_URL)

def create_HelloAllTypes():
    return HelloAllTypes(name="name", 
        all_types=create_AllTypes(),
        all_collection_types=create_AllCollectionTypes())

def create_AllTypes():
    return AllTypes(
        id=1,
        char='c',
        byte=2,
        short=3,
        int_=4,
        long=5,
        u_short=6,
        u_int=7,
        u_long=8,
        float=1.1,
        double=2.2,
        decimal=3.0,
        string="string",
        date_time=datetime(2001,1,1, tzinfo=timezone.utc),
        date_time_offset=datetime(2001,1,1, tzinfo=timezone.utc),
        time_span=timedelta(hours=1),
        guid="ea762009b66c410b9bf5ce21ad519249",
        string_list=["A", "B", "C"],
        string_array=["D", "E", "F"],
        string_map={"A":"D","B":"E","C":"F"},
        int_string_map={1:"A",2:"B",3:"C"},
        sub_type=SubType(id=1,name="name"))

def create_AllCollectionTypes():
    return AllCollectionTypes(
        int_array=[1,2,3],
        int_list=[1,2,3],
        string_array=["A","B","C"],
        string_list=["D","E","F"],
        byte_array=b"ABC", #base64(ABC)
        poco_array=[create_Poco("pocoArray")],
        poco_list=[create_Poco("pocoArray")],
        poco_lookup={"A":[create_Poco("B"),create_Poco("C")]},
        poco_lookup_map={"A":[{"B":create_Poco("C"),"D":create_Poco("E")}]})

def create_Poco(name:str): return Poco(name=name)

client = create_test_client()

class TestApi(unittest.TestCase):

    def assert_HelloAllTypesResponse(self,dto:HelloAllTypesResponse):
        # print(dto)
        self.assertEqual(dto.result,"name")
        self.assert_AllTypes(dto.all_types)
        self.assert_AllCollectionTypes(dto.all_collection_types)
        
    def assert_AllTypes(self,dto:AllTypes):
        # print(type(dto))
        # print(vars(dto))
        self.assertEqual(dto.id,1)
        self.assertEqual(dto.byte,2)
        self.assertEqual(dto.short,3)
        self.assertEqual(dto.int_,4)
        self.assertEqual(dto.long,5)
        self.assertEqual(dto.u_short,6)
        self.assertEqual(dto.u_int,7)
        self.assertEqual(dto.u_long,8)
        self.assertEqual(dto.float,1.1)
        self.assertEqual(dto.double,2.2)
        self.assertEqual(dto.decimal,3.0)
        self.assertEqual(dto.string,"string")
        self.assertEqual(dto.date_time,datetime(2001,1,1, tzinfo=timezone.utc))
        self.assertEqual(dto.date_time_offset,datetime(2001,1,1, tzinfo=timezone.utc))
        self.assertEqual(dto.time_span,timedelta(hours=1))
        self.assertEqual(dto.guid,"ea762009b66c410b9bf5ce21ad519249")
        self.assertListEqual(dto.string_list,["A", "B", "C"])
        self.assertListEqual(dto.string_array,["D", "E", "F"])
        self.assertDictEqual(dto.string_map,{"A":"D","B":"E","C":"F"})
        self.assertDictEqual(dto.int_string_map,{1:"A",2:"B",3:"C"})
        self.assertEqual(dto.sub_type.id,1)
        self.assertEqual(dto.sub_type.name,"name")

    def assert_AllCollectionTypes(self,dto:AllCollectionTypes):
        self.assertListEqual(dto.int_array,[1,2,3])
        self.assertListEqual(dto.int_list,[1,2,3])
        self.assertListEqual(dto.string_array,["A","B","C"])
        self.assertListEqual(dto.string_list,["D","E","F"])
        self.assertEqual(dto.byte_array,b'ABC')
        self.assertEqual(len(dto.poco_array),1)
        self.assertEqual(dto.poco_array[0].name,"pocoArray")
        self.assertEqual(len(dto.poco_lookup),1)
        poco_lookup_values=dto.poco_lookup["A"]
        self.assertEqual(len(poco_lookup_values),2)
        self.assertEqual(poco_lookup_values[0].name,"B")
        self.assertEqual(poco_lookup_values[1].name,"C")
        self.assertEqual(len(dto.poco_lookup_map),1)
        poco_lookup_map_values=dto.poco_lookup_map["A"]
        self.assertEqual(len(poco_lookup_map_values),1)
        poco_lookup_mapa_list=poco_lookup_map_values[0]
        self.assertEqual(len(poco_lookup_mapa_list),2)
        self.assertEqual(poco_lookup_mapa_list["B"].name,"C")
        self.assertEqual(poco_lookup_mapa_list["D"].name,"E")

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
        json_obj = client.post_url("/hello", to_json(Hello(name="World")))
        self.assertIsInstance(json_obj, dict)
        response = HelloResponse(**json_obj)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_HelloAllTypes(self):
        request=create_HelloAllTypes()
        response:HelloAllTypesResponse=client.post(request)
        self.assert_HelloAllTypesResponse(response)

    def test_can_put_HelloAllTypes(self):
        request=create_HelloAllTypes()
        response:HelloAllTypesResponse=client.put(request)
        self.assert_HelloAllTypesResponse(response)

    def test_does_handle_404_error(self):
        request = ThrowType(type="NotFound", message="not here")
        try:
            client.put(request)
            self.fail("should throw")
        except WebServiceException as ex:
            status = ex.response_status
            self.assertEqual(status.error_code, "NotFound")
            self.assertEqual(status.message, "not here")

