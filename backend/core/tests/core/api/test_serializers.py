from api.serializers import AgeSerializer, AuthorSerializer, PoemSerializer, TypeSerializer
from tests.fixtures import age, author, poem, type, user


import pytest


@pytest.mark.django_db
def test_age_serializer(age):
    age_serializer = AgeSerializer(age).data

    assert isinstance(age_serializer, dict)
    assert "name" in age_serializer


@pytest.mark.django_db
def test_author_serializer(author):
    author_serializer = AuthorSerializer(author).data

    assert isinstance(author_serializer, dict)
    assert "name" in author_serializer


@pytest.mark.django_db
def test_poem_serializer(poem):
    poem_serializer = PoemSerializer(poem).data

    assert isinstance(poem_serializer, dict)
    assert "age" in poem_serializer
    assert "author" in poem_serializer
    assert "content" in poem_serializer
    assert "title" in poem_serializer
    assert "type" in poem_serializer


@pytest.mark.django_db
def test_type_serializer(type):
    type_serializer = TypeSerializer(type).data

    assert isinstance(type_serializer, dict)
    assert "name" in type_serializer
