from servicestack import JsonServiceClient, Authenticate

# TEST_URL = "https://localhost:5001"
# TEST_URL = "http://localhost:5000"
TEST_URL = "http://test.servicestack.net"
TECHSTACKS_URL = "https://techstacks.io"

def create_test_client():
    return JsonServiceClient(TEST_URL)


def create_techstacks_client():
    return JsonServiceClient(TECHSTACKS_URL)


def clear_session(client: JsonServiceClient):
    client.post(Authenticate(provider="logout"))

