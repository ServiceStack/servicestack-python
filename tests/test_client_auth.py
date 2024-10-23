""" Auth Tests
"""

import unittest

from servicestack import WebServiceException
from .config import *
from .dtos import *


def create_jwt(**args) -> CreateJwt:
    to = CreateJwt(**args)
    if to.user_auth_id is None:
        to.user_auth_id = "1"
    if to.display_name is None:
        to.display_name = "test jwt"
    if to.email is None:
        to.email = "test@auth.com"
    return to


class State:
    count: int = 0

    def incr(self):
        self.count += 1


class TestAuthClient(unittest.TestCase):

    def test_can_auth_with_JWT(self):
        client = create_test_client()
        response: CreateJwtResponse = client.post(create_jwt())
        client.bearer_token = response.token

        test_auth: TestAuthResponse = client.get(TestAuth())
        self.assertEqual(test_auth.user_id, "1")
        self.assertEqual(test_auth.display_name, "test jwt")
        self.assertIsNotNone(test_auth.session_id)

    def test_does_fire_on_authentication_required_callback_on_401(self):
        client = create_test_client()
        state = State()

        client.on_authentication_required = lambda s=state: (s.incr())

        try:
            client.get(TestAuth())
            self.fail("should throw")
        except WebServiceException as e:
            status = e.response_status
            self.assertEqual(status.error_code, "401")
            self.assertEqual(status.message, "Unauthorized")
            self.assertEqual(state.count, 1)

    def test_can_use_on_authentication_required_to_auth_client(self):
        client = create_test_client()
        state = State()

        client.on_authentication_required = lambda c=client, s=state: [
            s.incr(),
            c.set_credentials("test", "test")
        ]

        client.get(TestAuth())
        self.assertEqual(state.count, 1)

    def test_can_use_on_authentication_required_to_fetch_token(self):
        client = create_test_client()
        state = State()
        auth_client = create_test_client()

        client.on_authentication_required = lambda c=client, a=auth_client, s=state: [
            s.incr(),
            a.post(Authenticate(provider="credentials", user_name="test", password="test")),
            client.set_bearer_token(a.refresh_token_cookie)
        ]

        client.get(TestAuth())
        self.assertEqual(state.count, 1)

    def test_can_use_on_authentication_required_to_fetch_token_after_expired_token(self):
        client = create_test_client()
        state = State()

        client.on_authentication_required = lambda c=client, s=state: [
            s.incr(),
            c.set_bearer_token(cast(CreateJwtResponse, c.post(create_jwt())).token)
        ]

        create_expired_jwt = create_jwt()
        create_expired_jwt.jwt_expiry = datetime.datetime(2000, 1, 1)
        expired_jwt: CreateJwtResponse = client.post(create_expired_jwt)

        client.bearer_token = expired_jwt.token
        client.get(TestAuth())
        self.assertEqual(state.count, 1)

    def test_can_use_refresh_token_to_fetch_token_after_expired_token(self):
        client = create_test_client()

        client.set_credentials("test", "test")
        auth_response: AuthenticateResponse = client.post(Authenticate())

        client.refresh_token = auth_response.refresh_token
        client.set_credentials(None, None)

        create_expired_jwt = create_jwt()
        create_expired_jwt.jwt_expiry = datetime.datetime(2000, 1, 1)
        expired_jwt: CreateJwtResponse = client.post(create_expired_jwt)

        client.bearer_token = expired_jwt.token
        client.get(TestAuth())
        #self.assertNotEqual(client.bearer_token, expired_jwt.token)

    def test_can_reauthenticate_after_an_auto_refresh_access_token(self):
        client = create_test_client()

        auth = Authenticate(provider="credentials", user_name="test", password="test")
        auth_response: AuthenticateResponse = client.post(auth)

        refresh_token = auth_response.refresh_token

        create_expired_jwt = create_jwt()
        create_expired_jwt.jwt_expiry = datetime.datetime(2000, 1, 1)
        expired_jwt: CreateJwtResponse = client.post(create_expired_jwt)
        bearer_token = expired_jwt.token

        clear_session(client)

        client = create_test_client()
        client.bearer_token = bearer_token
        client.refresh_token = refresh_token

        auth.password = "notvalid"
        try:
            client.post(auth)
            self.fail("should throw")
        except WebServiceException as e:
            status = e.response_status
            self.assertEqual(status.error_code, "Unauthorized")
            self.assertEqual(status.message, "Invalid Username or Password")

    def test_does_fetch_access_token_using_refresh_token_cookies(self):
        client = create_test_client()
        auth = Authenticate(provider="credentials", user_name="test", password="test")
        client.post(auth)

        initial_access_token = client.token_cookie
        initial_refresh_token = client.refresh_token_cookie
        self.assertIsNotNone(initial_access_token)
        self.assertIsNotNone(initial_refresh_token)

        request = Secured(name="test")
        response: SecuredResponse = client.send(request)
        self.assertEqual(response.result, request.name)

        client.post(InvalidateLastAccessToken())

        response: SecuredResponse = client.send(request)
        print(response)
        self.assertEqual(response.result, request.name)

        latest_access_token = client.token_cookie
        self.assertNotEqual(latest_access_token, initial_access_token)

    def test_invalid_refresh_token_throws_RefreshTokenException_ErrorResponse(self):
        client = create_test_client()

        client.refresh_token = "Invalid.Refresh.Token"

        try:
            client.get(TestAuth())
        except WebServiceException as e:
            self.assertEqual(e.type, WebServiceExceptionType.REFRESH_TOKEN_EXCEPTION)
            self.assertEqual(e.response_status.error_code, "ArgumentException")
            self.assertEqual(e.response_status.message, "Illegal base64url string!")

    def test_expires_refresh_token_throws_RefreshTokenException(self):
        client = create_test_client()

        create_expired_jwt = create_jwt()
        create_expired_jwt.jwt_expiry = datetime.datetime(2000, 1, 1)
        expired_jwt: CreateJwtResponse = client.post(create_expired_jwt)
        client.refresh_token = expired_jwt.token

        try:
            client.get(TestAuth())
        except WebServiceException as e:
            self.assertEqual(e.type, WebServiceExceptionType.REFRESH_TOKEN_EXCEPTION)
            self.assertEqual(e.response_status.error_code, "TokenException")
            self.assertEqual(e.response_status.message, "Token has expired")

