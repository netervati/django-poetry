from lib.mappers import ListMapper
from tests.fixtures import age


def test_clean_params_for_poem_exact(age):
    mapper = ListMapper([age]).to_dict()

    assert mapper["total_records"] == 1
    assert mapper["data"] == [age]
