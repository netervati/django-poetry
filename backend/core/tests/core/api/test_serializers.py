from api.serializers import (
    AuthorSerializer,
    ListSerializer,
    PoemByLineSerializer,
    PoemSerializer,
    RecordSerializer,
)
from lib.utils import map_data
from tests.fixtures import age, author, poem, user
from tests.helpers import assert_attributes_present

import pytest


@pytest.mark.django_db
def test_author_serializer(author):
    author_serializer = AuthorSerializer(author).data

    assert "name" in author_serializer


@pytest.mark.django_db
def test_poem_by_line_serializer(poem):
    poem_by_line_serializer = PoemByLineSerializer(poem).data

    assert_attributes_present(
        ["id", "age", "author_details", "lines", "title", "type"],
        poem_by_line_serializer,
    )


@pytest.mark.django_db
def test_poem_serializer(poem):
    poem_serializer = PoemSerializer(poem).data

    assert_attributes_present(
        ["id", "age", "author_details", "content", "title", "type"],
        poem_serializer,
    )


@pytest.mark.django_db
def test_list_serializer(age):
    list_mapper = map_data([age], list=True)
    list_serializer = ListSerializer(list_mapper).data

    assert_attributes_present(["total_records", "attributes"], list_serializer)


@pytest.mark.django_db
def test_record_serializer(age):
    record_mapper = map_data([age])
    record_serializer = RecordSerializer(record_mapper).data

    assert "attributes" in record_serializer
