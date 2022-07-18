from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)


from tests.fixtures import poem, user


import pytest


retrieve_poems_exact_url = reverse("retrieve-poems-exact")
retrieve_poems_like_url = reverse("retrieve-poems-like")


@pytest.mark.django_db
def test_retrieve_poems_exact_with_missing_params(client):
    response = client.get(retrieve_poems_exact_url)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.data["errors"] == ["You are missing valid query parameters."]


@pytest.mark.django_db
def test_retrieve_poems_exact_with_blank_params(client):
    response = client.get(retrieve_poems_exact_url, data={"title": ""})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.data["errors"][0]["title"] == "Parameter should not be blank."


@pytest.mark.django_db
def test_retrieve_poems_exact_with_no_return(client):
    response = client.get(retrieve_poems_exact_url, data={"title": "test"})

    assert response.status_code == HTTP_200_OK
    assert not response.data


@pytest.mark.django_db
def test_retrieve_poems_exact(client, poem):
    response = client.get(retrieve_poems_exact_url, data={"title": poem.title})

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.data, list)
    assert response.data[0]["age"] == poem.age
    assert response.data[0]["author"] == poem.author
    assert response.data[0]["content"] == poem.content
    assert response.data[0]["title"] == poem.title
    assert response.data[0]["type"] == poem.type


@pytest.mark.django_db
def test_retrieve_poems_like_with_missing_params(client):
    response = client.get(retrieve_poems_exact_url)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.data["errors"] == ["You are missing valid query parameters."]


@pytest.mark.django_db
def test_retrieve_poems_like_with_blank_params(client):
    response = client.get(retrieve_poems_like_url, data={"title": ""})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.data["errors"][0]["title"] == "Parameter should not be blank."


@pytest.mark.django_db
def test_retrieve_poems_like_with_no_return(client):
    response = client.get(retrieve_poems_like_url, data={"title": "test"})

    assert response.status_code == HTTP_200_OK
    assert not response.data


@pytest.mark.django_db
def test_retrieve_poems_like(client, poem):
    response = client.get(retrieve_poems_like_url, data={"title": poem.title[0:1]})

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.data, list)
    assert response.data[0]["age"] == poem.age
    assert response.data[0]["author"] == poem.author
    assert response.data[0]["content"] == poem.content
    assert response.data[0]["title"] == poem.title
    assert response.data[0]["type"] == poem.type
