from api.serializers import AuthorSerializer, PoemSerializer, ListSerializer
from tests.fixtures import age, author, poem, user
from lib.mappers import ListMapper

import pytest


@pytest.mark.django_db
def test_author_serializer(author):
    author_serializer = AuthorSerializer(author).data

    assert isinstance(author_serializer, dict)
    assert "name" in author_serializer


@pytest.mark.django_db
def test_poem_serializer(poem):
    poem_serializer = PoemSerializer(poem).data

    assert isinstance(poem_serializer, dict)
    assert "id" in poem_serializer
    assert "age" in poem_serializer
    assert "author" in poem_serializer
    assert "content" in poem_serializer
    assert "title" in poem_serializer
    assert "type" in poem_serializer


@pytest.mark.django_db
def test_list_serializer(age):
    list_mapper = ListMapper([age]).to_dict()
    list_serializer = ListSerializer(list_mapper).data

    assert "total_records" in list_serializer
    assert "data" in list_serializer
