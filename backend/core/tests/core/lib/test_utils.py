from db.models import Poem
from lib.utils import clean_params
from tests.fixtures import poem, user

import pytest


@pytest.fixture
def kwargs(poem):
    poem_dict = vars(poem)
    poem_dict['number'] = 'test'

    return poem_dict


@pytest.mark.django_db
def test_clean_params(kwargs):
    params = clean_params(kwargs, Poem)

    assert 'number' not in params
