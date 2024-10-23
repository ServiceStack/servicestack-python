""" TechStacks Tests
"""

import unittest

from .config import *
from .techstacks_dtos import *


class TestTechStacks(unittest.TestCase):

    def test_should_get_techs_response(self):
        client = create_techstacks_client()
        response: GetAllTechnologiesResponse = client.get(GetAllTechnologies())
        # print(response)
        self.assertGreater(len(response.results), 0)

    def test_should_get_techstacks_overview(self):
        client = create_techstacks_client()
        response: OverviewResponse = client.get(Overview())
        # print(response)
        self.assertGreater(len(response.top_technologies), 0)

    def test_should_throw_405(self):
        client = create_test_client()
        try:
            client.get(Overview())
            self.fail("should throw")
        except WebServiceException as e:
            self.assertEqual(e.status_code, 405)
            self.assertEqual(e.response_status.error_code, "NotImplementedException")
            self.assertEqual(e.response_status.message, "The operation does not exist for this service")

    def test_should_throw_401(self):
        client = create_techstacks_client()
        try:
            client.post(CreateTechnology())
            self.fail("should throw")
        except WebServiceException as e:
            self.assertEqual(e.status_code, 401)
            self.assertEqual(e.response_status.error_code, "401")
            self.assertEqual(e.response_status.message, "Unauthorized")

    def test_can_query_autoquery_with_runtime_args(self):
        client = create_techstacks_client()
        request = FindTechnologies(take=3)
        response = client.get(request, args={"VendorName": "Amazon"})
        results: list[TechnologyView] = response.results
        # print(results)
        self.assertEqual(len(results), 3)
        self.assertListEqual(
            list(map(lambda x: x.vendor_name, results)),
            ["Amazon", "Amazon", "Amazon"])

    def test_can_query_autoquery_with_anon_object_and_runtime_args(self):
        client = create_techstacks_client()
        args = {"Take": 3, "VendorName": "Amazon"}
        response = client.get_url("/technology/search", args=args,
                                  response_as=QueryResponse[TechnologyView])
        results: list[TechnologyView] = response.results
        # print(results)
        self.assertEqual(len(results), 3)
        self.assertListEqual(
            list(map(lambda x: x.vendor_name, results)),
            ["Amazon", "Amazon", "Amazon"])

    def test_can_query_with_args_and_base_class_property(self):
        client = create_techstacks_client()
        techs = client.get(FindTechnologies(), args={"slug": "flutter"})
        posts = client.get(QueryPosts(
            any_technology_ids=[techs.results[0].id],
            types=['Announcement', 'Showcase'],
            take=1))
        # print(results)
        self.assertEqual(techs.results[0].name, "Flutter")
        self.assertIsNotNone(posts.results[0].title)

