import os

import urllib3

from servicestack import JsonServiceClient, Authenticate

# TEST_URL = "https://localhost:5001"
# TEST_URL = "http://localhost:5000"
TEST_URL = "https://test.servicestack.net"
TECHSTACKS_URL = "https://techstacks.io"
# Load AI Server URL from environment variable
AI_SERVER_URL = os.getenv('AI_SERVER_URL')


def create_test_client():
    return JsonServiceClient(TEST_URL)


def create_techstacks_client():
    return JsonServiceClient(TECHSTACKS_URL)


def clear_session(client: JsonServiceClient):
    client.post(Authenticate(provider="logout"))


def create_aiserver_client():
    """Create a client for AI Server tests using environment variables"""
    url = os.getenv('AI_SERVER_URL')
    api_key = os.getenv('AI_SERVER_API_KEY')

    if not url or not api_key:
        raise EnvironmentError(
            "AI_SERVER_URL and AI_SERVER_API_KEY environment variables are required. "
            "Please set these before running the AI server tests."
        )

    client = JsonServiceClient(url)
    client.set_bearer_token(api_key)

    return client

def log():
    pass