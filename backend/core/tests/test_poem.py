from multiprocessing.sharedctypes import Array

from django.http import JsonResponse
from tests.fixtures import poem, user
from django.urls import reverse


import pytest


retrieve_poems_url = reverse("retrieve-poems")


@pytest.mark.django_db
def test_retrieve_poems_with_missing_params(client):
    response = client.get(retrieve_poems_url)

    assert response.status_code == 400
    assert response.data["errors"] == ["You are missing valid query parameters."]


@pytest.mark.django_db
def test_retrieve_poems_with_blank_params(client):
    response = client.get(retrieve_poems_url, data={"title": ""})

    assert response.status_code == 400
    assert response.data["errors"][0]["title"] == "Parameter should not be blank."


@pytest.mark.django_db
def test_retrieve_poems(client, poem):
    response = client.get(retrieve_poems_url, data={"title": poem.title})

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert response.data[0]["age"] == poem.age
    assert response.data[0]["author"] == poem.author
    assert response.data[0]["content"] == poem.content
    assert response.data[0]["title"] == poem.title
    assert response.data[0]["type"] == poem.type
