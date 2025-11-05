import pytest
from helpers.api_client import ApiClient
from data.user_data import generate_user

@pytest.fixture(scope="session")
def client():
    return ApiClient()


@pytest.fixture
def new_user(client):

    user = generate_user()
    client.post("/auth/register", user)

    res = client.post("/auth/login", {"email": user["email"], "password": user["password"]})
    token = res.json().get("accessToken")
    headers = {"Authorization": token}

    yield {"user": user, "headers": headers}

    client.delete("/auth/user", headers=headers)
