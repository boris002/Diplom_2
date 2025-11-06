import pytest
from helpers.api_client import ApiClient
from data.user_data import generate_user
from data.urls import BaseURL, AuthEndpoints

@pytest.fixture(scope="session")
def client():
    return ApiClient(BaseURL.BASE)


@pytest.fixture
def new_user(client):

    user = generate_user()
    client.post(AuthEndpoints.REGISTER, user)

    res = client.post(AuthEndpoints.LOGIN, {"email": user["email"], "password": user["password"]})
    token = res.json().get("accessToken")
    headers = {"Authorization": token}

    yield {"user": user, "headers": headers}

    client.delete(AuthEndpoints.DELETE_USER, headers=headers)
