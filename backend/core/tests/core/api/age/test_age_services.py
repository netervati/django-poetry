from django.urls import reverse
from rest_framework.status import HTTP_200_OK


import pytest


# TO-DO feat_v1.0007: Mock lib.utils.StandingData
@pytest.mark.django_db
def test_retrieve_ages(client):
    response = client.get(reverse("retrieve-ages"))

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.data, dict)
    assert isinstance(response.data["data"], list)
