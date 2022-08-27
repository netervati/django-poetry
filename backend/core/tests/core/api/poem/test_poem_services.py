from rest_framework.exceptions import ValidationError


from api.poem.poem_services import (
    RetrievePoemsExactService,
    RetrievePoemsLikeService,
    RetrievePoemService,
)
from tests.fixtures import author, fake_request, poem, user
from tests.helpers import model_fixture_to_dict


import pytest


base_path = "api.poem.poem_services."


@pytest.mark.django_db
def test_retrieve_poems_exact_service(mocker, poem, fake_request):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}clean_params").return_value = poem_dict
    mocker.patch(f"{base_path}Validation.run").return_value = None
    mocker.patch(f"{base_path}set_filter").return_value = {}
    mocker.patch(f"{base_path}Poem").objects.filter.return_value = poem_dict

    subject = RetrievePoemsExactService(fake_request)

    assert subject.run() == {"by-line": False, "poem": poem_dict}

    mocker.patch(f"{base_path}Validation.run").return_value = "error"

    with pytest.raises(ValidationError):
        subject.run()


@pytest.mark.django_db
def test_retrieve_poems_like_service(mocker, poem, fake_request):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}clean_params").return_value = poem_dict
    mocker.patch(f"{base_path}Validation.run").return_value = None
    mocker.patch(f"{base_path}set_filter").return_value = {}
    mocker.patch(f"{base_path}Poem").objects.filter.return_value = poem_dict

    subject = RetrievePoemsLikeService(fake_request)

    assert subject.run() == {"by-line": False, "poem": poem_dict}

    mocker.patch(f"{base_path}Validation.run").return_value = "error"

    with pytest.raises(ValidationError):
        subject.run()


@pytest.mark.django_db
def test_retrieve_poem_service(mocker, fake_request, poem):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}clean_params").return_value = poem_dict
    mocker.patch(f"{base_path}Validation.run").return_value = None
    mocker.patch(f"{base_path}Poem").objects.get.return_value = poem_dict

    subject = RetrievePoemService(poem.id, fake_request)

    assert subject.run() == {"by-line": False, "poem": poem_dict}

    mocker.patch(f"{base_path}Poem").objects.get.side_effect = ValidationError

    with pytest.raises(ValidationError):
        subject.run()
