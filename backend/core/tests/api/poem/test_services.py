from multiprocessing.sharedctypes import Array

from django.http import JsonResponse
from tests.fixtures import poem, user
from django.urls import reverse


import pytest


@pytest.mark.django_db
def test_retrieve_poems(client, poem):
    url = reverse("get-poems")
    response = client.get(url, data={"title": poem.title})

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert response.data[0]["age"] == poem.age
    assert response.data[0]["author"] == poem.author
    assert response.data[0]["content"] == poem.content
    assert response.data[0]["title"] == poem.title
    assert response.data[0]["type"] == poem.type
