from lib.rules import ALLOWED_ATTR_FOR_AUTHOR
from lib.utils import clean_params, match_like, Validation
from tests.fixtures import author, user
from tests.helpers import assert_attributes_not_present


import pytest


@pytest.mark.django_db
def author_kwargs(author):
    author_dict = vars(author)
    author_dict["ignore"] = "test"

    return author_dict


@pytest.mark.django_db
def test_clean_params(author):
    params = clean_params(author_kwargs(author), ALLOWED_ATTR_FOR_AUTHOR)

    assert_attributes_not_present(
        ["ignore", "created_at", "updated_at", "user_id"], params
    )


def test_match_like():
    params = match_like({"test": "data"})

    assert params["test__icontains"] == "data"


def test_blank_validation():
    params = Validation({"test": ""})
    error = params.run(["blank_params"])

    assert error[0] == {"test": "Parameter should not be blank."}


def test_required_validation():
    params = Validation({})
    error = params.run(["missing_params"])

    assert error[0] == "You are missing valid query parameters."
