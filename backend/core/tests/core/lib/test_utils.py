from db.models import Poem
from lib.utils import clean_params
from tests.fixtures import poem, user

import pytest


@pytest.fixture
def kwargs(poem):
    poem_dict = vars(poem)
    poem_dict["id"] = "test"
    poem_dict["ignore"] = "test"
    poem_dict["created_at"] = "test"
    poem_dict["updated_at"] = "test"
    poem_dict["user_id"] = "test"

    return poem_dict


@pytest.mark.django_db
def test_clean_params(kwargs):
    params = clean_params(kwargs, Poem)

    assert "id" not in params
    assert "ignore" not in params
    assert "created_at" not in params
    assert "updated_at" not in params
    assert "user_id" not in params
