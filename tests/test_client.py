""" Basic Serialization Tests
"""

import unittest
import dataclasses
import datetime
import json
import io
from .dtos import *
from servicestack import JsonServiceClient, WebServiceException, to_json
from .config import create_test_client



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
        float_=1.1,
        double=2.2,
        decimal=decimal.Decimal(3.0),
        string="string",
        date_time=datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc),
        date_time_offset=datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc),
        time_span=datetime.timedelta(hours=1),
        guid="ea762009b66c410b9bf5ce21ad519249",
        string_list=["A", "B", "C"],
        string_array=["D", "E", "F"],
        string_map={"A": "D", "B": "E", "C": "F"},
        int_string_map={1: "A", 2: "B", 3: "C"},
        sub_type=SubType(id=1, name="name"))


def create_AllCollectionTypes():
    return AllCollectionTypes(
        int_array=[1, 2, 3],
        int_list=[1, 2, 3],
        string_array=["A", "B", "C"],
        string_list=["D", "E", "F"],
        byte_array=b"ABC",  # base64(ABC)
        poco_array=[create_Poco("pocoArray")],
        poco_list=[create_Poco("pocoArray")],
        poco_lookup={"A": [create_Poco("B"), create_Poco("C")]},
        poco_lookup_map={"A": [{"B": create_Poco("C"), "D": create_Poco("E")}]})


def create_Poco(name: str): return Poco(name=name)


def create_EchoComplexTypes():
    return EchoComplexTypes(
        sub_type=SubType(id=1, name="foo"),
        sub_types=[SubType(id=2, name="bar"), SubType(id=3, name="baz")],
        sub_type_map={
            "a": SubType(id=4, name="qux")
        },
        string_map={
            "a": "b"
        },
        int_string_map={
            1: "A"
        }
    )


def assert_AllTypes(test: unittest.TestCase, dto: AllTypes):
    # print(type(dto))
    # print(vars(dto))
    test.assertEqual(dto.id, 1)
    test.assertEqual(dto.byte, 2)
    test.assertEqual(dto.short, 3)
    test.assertEqual(dto.int_, 4)
    test.assertEqual(dto.long, 5)
    test.assertEqual(dto.u_short, 6)
    test.assertEqual(dto.u_int, 7)
    test.assertEqual(dto.u_long, 8)
    test.assertEqual(dto.float_, 1.1)
    test.assertEqual(dto.double, 2.2)
    test.assertEqual(dto.decimal, 3.0)
    test.assertEqual(dto.string, "string")
    test.assertEqual(dto.date_time, datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc))
    test.assertEqual(dto.date_time_offset, datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc))
    test.assertEqual(dto.time_span, datetime.timedelta(hours=1))
    test.assertEqual(dto.guid, "ea762009b66c410b9bf5ce21ad519249")
    test.assertListEqual(dto.string_list, ["A", "B", "C"])
    test.assertListEqual(dto.string_array, ["D", "E", "F"])
    test.assertDictEqual(dto.string_map, {"A": "D", "B": "E", "C": "F"})
    test.assertDictEqual(dto.int_string_map, {1: "A", 2: "B", 3: "C"})
    test.assertEqual(dto.sub_type.id, 1)
    test.assertEqual(dto.sub_type.name, "name")


def assert_AllCollectionTypes(test: unittest.TestCase, dto: AllCollectionTypes):
    test.assertListEqual(dto.int_array, [1, 2, 3])
    test.assertListEqual(dto.int_list, [1, 2, 3])
    test.assertListEqual(dto.string_array, ["A", "B", "C"])
    test.assertListEqual(dto.string_list, ["D", "E", "F"])
    test.assertEqual(dto.byte_array, b'ABC')
    test.assertEqual(len(dto.poco_array), 1)
    test.assertEqual(dto.poco_array[0].name, "pocoArray")
    test.assertEqual(len(dto.poco_lookup), 1)
    poco_lookup_values = dto.poco_lookup["A"]
    test.assertEqual(len(poco_lookup_values), 2)
    test.assertEqual(poco_lookup_values[0].name, "B")
    test.assertEqual(poco_lookup_values[1].name, "C")
    test.assertEqual(len(dto.poco_lookup_map), 1)
    poco_lookup_map_values = dto.poco_lookup_map["A"]
    test.assertEqual(len(poco_lookup_map_values), 1)
    poco_lookup_mapa_list = poco_lookup_map_values[0]
    test.assertEqual(len(poco_lookup_mapa_list), 2)
    test.assertEqual(poco_lookup_mapa_list["B"].name, "C")
    test.assertEqual(poco_lookup_mapa_list["D"].name, "E")


client = create_test_client()


class TestApi(unittest.TestCase):

    def assert_HelloAllTypesResponse(self, dto: HelloAllTypesResponse):
        # print(dto)
        self.assertEqual(dto.result, "name")
        self.assert_AllTypes(dto.all_types)
        self.assert_AllCollectionTypes(dto.all_collection_types)

    def assert_AllTypes(self, dto: AllTypes): assert_AllTypes(self, dto)

    def assert_AllCollectionTypes(self, dto: AllCollectionTypes):
        assert_AllCollectionTypes(self, dto)

    def assert_EchoComplexTypes(self, dto: EchoComplexTypes):
        self.assertEqual(dto.sub_type.id, 1)
        self.assertEqual(dto.sub_type.name, "foo")
        self.assertEqual(dto.sub_types[0].id, 2)
        self.assertEqual(dto.sub_types[0].name, "bar")
        self.assertEqual(dto.sub_types[1].id, 3)
        self.assertEqual(dto.sub_types[1].name, "baz")
        self.assertEqual(dto.sub_type_map["a"].id, 4)
        self.assertEqual(dto.sub_type_map["a"].name, "qux")
        self.assertEqual(dto.string_map["a"], "b")
        self.assertEqual(dto.int_string_map[1], "A")

    def test_can_get_hello(self):
        response: HelloResponse = client.get(Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_hello(self):
        response: HelloResponse = client.post(Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_send_umlauts(self):
        response: HelloResponse = client.post(Hello(name="üöäß"))
        self.assertEqual(response.result, "Hello, üöäß!")

    def test_does_fire_Request_and_Response_filters(self):
        client = create_test_client()
        events = []

        JsonServiceClient.global_request_filter = lambda info: events.append("globalRequestFilter")
        JsonServiceClient.global_response_filter = lambda res: events.append("globalResponseFilter")

        client.request_filter = lambda info: events.append("requestFilter")
        client.response_filter = lambda res: events.append("responseFilter")

        response: HelloResponse = client.get(Hello(name="World"))
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
        response: HelloResponse = client.get_url("/hello/World", response_as=HelloResponse)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_get_hello_with_CustomPath_as_raw_types(self):
        json_str = client.get_url("/hello", response_as=str, args={'name': 'World'})
        self.assertEqual(json_str, '{"result":"Hello, World!"}')

        json_bytes: bytes = client.get_url("/hello", response_as=bytes, args={'name': 'World'})
        self.assertEqual(json_bytes.decode("utf-8"), '{"result":"Hello, World!"}')

        dto: HelloResponse = client.get_url("/hello", response_as=HelloResponse, args={'name': 'World'})
        self.assertEqual(dto.result, "Hello, World!")

    def test_can_post_Hello_with_CustomPath(self):
        response: HelloResponse = client.post_url("/hello", Hello(name="World"))
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_hello_with_CustomPath_json_object(self):
        json_obj = client.post_url("/hello", to_json(Hello(name="World")))
        self.assertIsInstance(json_obj, dict)
        response = HelloResponse(**json_obj)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_post_HelloAllTypes(self):
        request = create_HelloAllTypes()
        response: HelloAllTypesResponse = client.post(request)
        self.assert_HelloAllTypesResponse(response)

    def test_can_put_HelloAllTypes(self):
        request = create_HelloAllTypes()
        response: HelloAllTypesResponse = client.put(request)
        self.assert_HelloAllTypesResponse(response)

    def test_can_use_base_url_with_path(self):
        custom_client = JsonServiceClient("https://openai.servicestack.net/v1/")
        self.assertTrue(custom_client.base_url.startswith("https://openai.servicestack.net"))
        self.assertIn("/v1",custom_client.reply_base_url)
        self.assertIn("/v1",custom_client.oneway_base_url)

        custom_client = JsonServiceClient("https://openai.servicestack.net")
        self.assertTrue(custom_client.base_url.startswith("https://openai.servicestack.net"))
        self.assertTrue(custom_client.reply_base_url.endswith("/api/"))
        self.assertTrue(custom_client.oneway_base_url.endswith("/api/"))



    def test_does_handle_404_error(self):
        request = ThrowType(type="NotFound", message="not here")
        try:
            client.put(request)
            self.fail("should throw")
        except WebServiceException as ex:
            status = ex.response_status
            self.assertEqual(status.error_code, "NotFound")
            self.assertEqual(status.message, "not here")

    def test_does_handle_ValidationException(self):
        request = ThrowValidation(email="invalidemail")
        try:
            client.post(request)
            self.fail("should throw")
        except WebServiceException as ex:
            status = ex.response_status
            errors = status.errors
            self.assertEqual(len(errors), 3)
            self.assertEqual(errors[0].error_code, status.error_code)
            self.assertEqual(errors[0].message, status.message)

            self.assertEqual(errors[0].error_code, "InclusiveBetween")
            self.assertEqual(errors[0].message, "'Age' must be between 1 and 120. You entered 0.")
            self.assertEqual(errors[0].field_name, "Age")

            self.assertEqual(errors[1].error_code, "NotEmpty")
            self.assertEqual(errors[1].message, "'Required' must not be empty.")
            self.assertEqual(errors[1].field_name, "Required")

            self.assertEqual(errors[2].error_code, "Email")
            self.assertEqual(errors[2].message, "'Email' is not a valid email address.")
            self.assertEqual(errors[2].field_name, "Email")

    def test_does_handle_auth_failure(self):
        request = RequiresAdmin()
        try:
            client.post(request)
            self.fail("should throw")
        except WebServiceException as ex:
            self.assertEqual(ex.status_code, 401)

    def test_can_send_ReturnVoid(self):
        client = create_test_client()
        sent_methods = []
        client.request_filter = lambda req: sent_methods.append(req.method)

        request = SendReturnVoid(id=1)
        client.send(request)
        self.assertEqual(sent_methods[-1], "POST")
        request.id = 2
        client.get(request)
        self.assertEqual(sent_methods[-1], "GET")
        request.id = 3
        client.post(request)
        self.assertEqual(sent_methods[-1], "POST")
        request.id = 4
        client.put(request)
        self.assertEqual(sent_methods[-1], "PUT")
        request.id = 5
        client.delete(request)
        self.assertEqual(sent_methods[-1], "DELETE")

    def test_can_get_response_as_Raw_String(self):
        response = client.get(HelloString(name="World"))
        self.assertEqual(response, "World")

    def test_can_get_response_as_Raw_Bytes(self):
        response = client.get_url("/json/reply/HelloString?Name=World", response_as=bytes)
        self.assertEqual(response.decode("utf-8"), "World")

    def test_should_return_raw_text(self):
        response = client.get(ReturnString(data="0x10"))
        self.assertEqual(response, "0x10")

    def test_can_send_raw_json_as_object(self):
        client = create_test_client()
        client.response_filter = lambda res: self.assertEqual(res.headers["X-Args"], "1,name")

        body = {"foo": "bar"}
        request = SendJson(id=1, name="name")

        json_str = client.post(request, body=to_json(body))
        json_obj = json.loads(json_str)

        self.assertEqual(json_obj["foo"], "bar")

    def test_can_send_raw_string(self):
        client = create_test_client()
        client.response_filter = lambda res: self.assertEqual(res.headers["X-Args"], "1,name")
        body = "foo"
        request = SendText(id=1, name="name", content_type="text/plain")
        str = client.post(request, body=body)
        self.assertEqual(str, "foo")

    def test_can_deserialize_nested_list(self):
        client = create_test_client()
        response: Items = client.get(GetItems())
        self.assertEqual(len(response.results), 2)

        all_names = list(map(lambda x: x.name, response.results))
        self.assertLessEqual(all_names, ["bar item 1", "bar item 2"])

    def test_can_deserialize_naked_list(self):
        client = create_test_client()
        response: List[Item] = client.get(GetNakedItems())
        self.assertEqual(len(response), 2)
        all_names = list(map(lambda x: x.name, response))
        self.assertLessEqual(all_names, ["item 1", "item 2"])

    def test_can_deserialize_custom_generic_response_type(self):
        response: QueryResponseAlt[Item] = client.get(AltQueryItems())
        self.assertEqual(len(response.results), 2)
        all_names = list(map(lambda x: x.name, response.results))
        self.assertLessEqual(all_names, ["item 1", "item 2"])

    # requires Python 3.9
    def test_can_send_all_batch_request(self):
        client = create_test_client()
        client.response_filter = lambda res: self.assertEqual(res.headers["X-AutoBatch-Completed"], "3")
        requests = list(map(lambda name: Hello(name=name), ["foo", "bar", "baz"]))
        responses = client.send_all(requests)
        self.assertListEqual(list(map(lambda x: x.result, responses)),
                             ['Hello, foo!', 'Hello, bar!', 'Hello, baz!'])

    # requires Python 3.9
    def test_can_send_all_oneway_IReturn_batch_request(self):
        client = create_test_client()
        client.request_filter = lambda req: self.assertTrue(req.url.endswith("/api/Hello[]"))
        requests = list(map(lambda name: Hello(name=name), ["foo", "bar", "baz"]))
        client.send_all_oneway(requests)

    # requires Python 3.9
    def test_can_send_all_oneway_IReturnVoid_batch_request(self):
        client = create_test_client()
        client.request_filter = lambda req: self.assertTrue(req.url.endswith("/api/HelloReturnVoid[]"))
        requests = list(map(lambda name: HelloReturnVoid(name=name), [1, 2, 3]))
        client.send_all_oneway(requests)

    def test_can_post_to_EchoTypes(self):
        response: EchoTypes = client.post(EchoTypes(int_=1, string="foo"))
        self.assertEqual(response.int_, 1)
        self.assertEqual(response.string, "foo")

    def test_can_get_IReturnVoid_requests(self):
        client.get(HelloReturnVoid(id=1))

    def test_can_post_IReturnVoid_requests(self):
        client.post(HelloReturnVoid(id=1))

    def test_can_handle_Validation_Errors_with_camelcasing(self):
        client = create_test_client()
        client.request_filter = lambda req: self.assertTrue(
            req.url.endswith("ThrowValidation?jsconfig=EmitCamelCaseNames%3Atrue"))
        try:
            client.post(ThrowValidation(), args={"jsconfig": "EmitCamelCaseNames:true"})
        except WebServiceException as e:
            self.assertEqual(e.response_status.error_code, "InclusiveBetween")
            self.assertEqual(e.response_status.message, "'Age' must be between 1 and 120. You entered 0.")
            self.assertEqual(e.response_status.errors[1].error_code, "NotEmpty")
            self.assertEqual(e.response_status.errors[1].field_name, "Required")
            self.assertEqual(e.response_status.errors[1].message, "'Required' must not be empty.")

    def test_can_handle_Validation_Errors_with_pascalcasing(self):
        client = create_test_client()
        client.request_filter = lambda req: self.assertTrue(
            req.url.endswith("ThrowValidation?jsconfig=EmitCamelCaseNames%3Afalse"))
        try:
            client.post(ThrowValidation(), args={"jsconfig": "EmitCamelCaseNames:false"})
        except WebServiceException as e:
            self.assertEqual(e.response_status.error_code, "InclusiveBetween")
            self.assertEqual(e.response_status.message, "'Age' must be between 1 and 120. You entered 0.")
            self.assertEqual(e.response_status.errors[1].error_code, "NotEmpty")
            self.assertEqual(e.response_status.errors[1].field_name, "Required")
            self.assertEqual(e.response_status.errors[1].message, "'Required' must not be empty.")

    def test_can_get_using_only_path_info(self):
        response: HelloResponse = client.get_url("/hello/World", response_as=HelloResponse)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_get_using_absolute_url(self):
        response: HelloResponse = client.get_url("https://test.servicestack.net/hello/World", response_as=HelloResponse)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_get_using_route_and_querystring(self):
        response: HelloResponse = client.get_url("/hello", args={"name": "World"}, response_as=HelloResponse)
        self.assertEqual(response.result, "Hello, World!")

    def test_can_get_EchoTypes_using_route(self):
        request = EchoTypes(long=1, string="foo")
        args = dataclasses.asdict(request)
        response: EchoTypes = client.get_url("/echo/types", args=args, response_as=EchoTypes)
        self.assertEqual(response.long, 1)
        self.assertEqual(response.string, "foo")

    def test_can_post_EchoComplexTypes(self):
        request = create_EchoComplexTypes()
        response = client.post(request)
        self.assert_EchoComplexTypes(response)

    def test_can_handle_connection_error(self):
        client = JsonServiceClient("http://unknown-zzz.net")

        client.exception_filter = lambda res, e: (
            # print(e.status_code) and
            # print(e.status_description)
        )
        try:
            client.get(EchoTypes(int_=1, string="foo"))
        except WebServiceException as e:
            self.assertEqual(e.status_code, 500)
            self.assertIn("Max retries exceeded with url", e.status_description)
            # self.assertTrue("getaddrinfo failed" in handled_ex.status_description)
        except e:
            self.fail("Expected WebServiceException")

    def test_can_handle_naked_List(self):
        request = HelloList(names=['A', 'B', 'C'])
        response: List[ListResult] = client.get(request)
        self.assertEqual(len(response), 3)

    def test_upload_with_complex_request_dto(self):
        all_collection_types=create_AllCollectionTypes()        
        dto = TestUploadWithDto(
            int_=1,
            nullable_id=None,
            long=2,
            double=4.0,
            string='string',
            date_time=datetime.datetime(1, 1, 1, tzinfo=datetime.timezone.utc),
            int_array=all_collection_types.int_array,
            int_list=all_collection_types.int_list,
            string_array=all_collection_types.string_array,
            string_list=all_collection_types.string_list,
            poco_array=all_collection_types.poco_array,
            poco_list=all_collection_types.poco_list,
            poco_lookup=all_collection_types.poco_lookup,
            poco_lookup_map=all_collection_types.poco_lookup_map,
            map_list={
              'A': ['a', 'b', 'c'],
              'B': ['d', 'e', 'f']
            },
        )

        # print("\nREQUEST:")
        # print(to_jsv_data(dto))

        response = client.post_file_with_request(
            request=dto, 
            file=UploadFile(
                field_name="image",
                file_name="test_image.png",
                content_type="image/png",
                stream=io.BytesIO()
            ))

        # print("\nRESPONSE:")
        # print(response)
        
        self.assertEqual(response.int_, dto.int_)
        self.assertEqual(response.nullable_id, dto.nullable_id)
        self.assertEqual(response.long, dto.long)
        self.assertEqual(response.double, dto.double)
        self.assertEqual(response.string, dto.string)
        self.assertEqual(response.date_time, dto.date_time)

        self.assertListEqual(response.int_array, dto.int_array)
        self.assertListEqual(response.string_array, dto.string_array)
        self.assertListEqual(response.string_list, dto.string_list)
        self.assertEqual(len(response.poco_array), len(dto.poco_array))
        self.assertEqual(response.poco_array[0].name, dto.poco_array[0].name)

        self.assertEqual(len(response.poco_lookup), len(dto.poco_lookup))
        self.assertEqual(response.poco_lookup["A"][0].name, dto.poco_lookup["A"][0].name)
        self.assertEqual(response.poco_lookup["A"][1].name, dto.poco_lookup["A"][1].name)

        self.assertEqual(len(response.poco_lookup_map), 1)
        poco_lookup_map_values = response.poco_lookup_map["A"]
        self.assertEqual(len(poco_lookup_map_values), 1)
        poco_lookup_mapa_list = poco_lookup_map_values[0]
        self.assertEqual(len(poco_lookup_mapa_list), 2)
        self.assertEqual(poco_lookup_mapa_list["B"].name, "C")
        self.assertEqual(poco_lookup_mapa_list["D"].name, "E")

        self.assertEqual(len(response.map_list), len(dto.map_list))
        self.assertListEqual(response.map_list['A'], dto.map_list['A'])
        self.assertListEqual(response.map_list['B'], dto.map_list['B'])
