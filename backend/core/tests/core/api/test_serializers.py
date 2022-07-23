from api.serializers import (
    AuthorSerializer,
    ListSerializer,
    PoemByLineSerializer,
    PoemSerializer,
    RecordSerializer,
)
from lib.mappers import ListMapper, RecordMapper
from tests.fixtures import age, author, poem, user


import pytest


@pytest.mark.django_db
def test_author_serializer(author):
    author_serializer = AuthorSerializer(author).data

    assert isinstance(author_serializer, dict)
    assert "name" in author_serializer


@pytest.mark.django_db
def test_poem_by_line_serializer(poem):
    poem_by_line_serializer = PoemByLineSerializer(poem).data

    assert isinstance(poem_by_line_serializer, dict)
    assert "id" in poem_by_line_serializer
    assert "age" in poem_by_line_serializer
    assert "author_details" in poem_by_line_serializer
    assert "lines" in poem_by_line_serializer
    assert "title" in poem_by_line_serializer
    assert "type" in poem_by_line_serializer


@pytest.mark.django_db
def test_poem_serializer(poem):
    poem_serializer = PoemSerializer(poem).data

    assert isinstance(poem_serializer, dict)
    assert "id" in poem_serializer
    assert "age" in poem_serializer
    assert "author_details" in poem_serializer
    assert "content" in poem_serializer
    assert "title" in poem_serializer
    assert "type" in poem_serializer


@pytest.mark.django_db
def test_list_serializer(age):
    list_mapper = ListMapper([age]).to_dict()
    list_serializer = ListSerializer(list_mapper).data

    assert "total_records" in list_serializer
    assert "attributes" in list_serializer


@pytest.mark.django_db
def test_record_serializer(age):
    record_mapper = RecordMapper([age]).to_dict()
    record_serializer = RecordSerializer(record_mapper).data

    assert "attributes" in record_serializer
