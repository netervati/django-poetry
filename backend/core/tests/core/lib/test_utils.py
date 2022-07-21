from lib.mappers import (
    ALLOWED_ATTR_FOR_AUTHOR,
    ALLOWED_ATTR_FOR_POEM_EXACT,
    ALLOWED_ATTR_FOR_POEM_LIKE,
)
from lib.utils import clean_params
from tests.fixtures import author, poem, user


import pytest


@pytest.fixture
def author_kwargs(author):
    author_dict = vars(author)
    author_dict["ignore"] = "test"

    return author_dict


@pytest.fixture
def poem_kwargs(poem):
    poem_dict = vars(poem)
    poem_dict["ignore"] = "test"

    return poem_dict


@pytest.mark.django_db
def test_clean_params_for_authors(author_kwargs):
    params = clean_params(author_kwargs, ALLOWED_ATTR_FOR_AUTHOR)

    assert "ignore" not in params
    assert "created_at" not in params
    assert "updated_at" not in params
    assert "user_id" not in params


@pytest.mark.django_db
def test_clean_params_for_poem_exact(poem_kwargs):
    params = clean_params(poem_kwargs, ALLOWED_ATTR_FOR_POEM_EXACT)

    assert "content" not in params
    assert "id" not in params
    assert "ignore" not in params
    assert "created_at" not in params
    assert "updated_at" not in params
    assert "user_id" not in params


@pytest.mark.django_db
def test_clean_params_for_poem_like(poem_kwargs):
    params = clean_params(poem_kwargs, ALLOWED_ATTR_FOR_POEM_LIKE)

    assert "content" in params
    assert "id" not in params
    assert "ignore" not in params
    assert "created_at" not in params
    assert "updated_at" not in params
    assert "user_id" not in params
