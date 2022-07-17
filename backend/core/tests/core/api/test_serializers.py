from api.serializers import PoemSerializer
from tests.fixtures import poem, user


import pytest


@pytest.mark.django_db
def test_poem_serializer(poem):
    poem_serializer = PoemSerializer(poem).data

    assert isinstance(poem_serializer, dict)
    assert "age" in poem_serializer
    assert "author" in poem_serializer
    assert "content" in poem_serializer
    assert "title" in poem_serializer
    assert "type" in poem_serializer
