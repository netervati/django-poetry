from django.urls import reverse
from rest_framework.status import HTTP_200_OK


import pytest


@pytest.mark.django_db
def test_retrieve_types(client):
    response = client.get(reverse("retrieve-types"))

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.data, dict)
    assert isinstance(response.data["attributes"], list)
