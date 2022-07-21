from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)


from tests.fixtures import author, user


import pytest


retrieve_authors_url = reverse("retrieve-authors")


@pytest.mark.django_db
def test_retrieve_authors_with_blank_params(client):
    response = client.get(retrieve_authors_url, data={"name": ""})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.data["errors"][0]["name"] == "Parameter should not be blank."


@pytest.mark.django_db
def test_retrieve_authors_with_no_return(client):
    response = client.get(retrieve_authors_url, data={"name": "xxx"})

    assert response.status_code == HTTP_200_OK
    assert not response.data["data"]


@pytest.mark.django_db
def test_retrieve_authors(client, author):
    response = client.get(retrieve_authors_url, data={"name": author.name})

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.data, dict)
    assert isinstance(response.data["data"], list)
    assert response.data["total_records"] == 1
    assert response.data["data"][0]["id"] == str(author.id)
    assert response.data["data"][0]["name"] == author.name
