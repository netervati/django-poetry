from api.serializers import AuthorSerializer
from lib.mappers import RecordMapper, ListMapper
from tests.fixtures import age, author, user


import pytest


def test_list_mapper(age):
    mapper = ListMapper([age]).to_dict()

    assert mapper["total_records"] == 1
    assert mapper["attributes"] == [age]


@pytest.mark.django_db
def test_record_mapper(author):
    mapper = RecordMapper(AuthorSerializer(author).data).to_dict()

    assert mapper["attributes"]["name"] == author.name
