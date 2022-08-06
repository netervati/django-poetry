from api.poem.poem_controller import PoemController
from tests.fixtures import author, fake_request, poem, user
from tests.helpers import assert_responses_match, model_fixture_to_dict


import pytest


base_path = "api.poem.poem_controller."


@pytest.mark.django_db
def test_poem_controller_retrieve_exact(mocker, poem):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}RetrievePoemsExactService").run.return_value = poem_dict
    mocker.patch(f"{base_path}PoemByLineSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}PoemSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}render").return_value = poem_dict

    assert_responses_match(PoemController().retrieve_exact(""), poem_dict)


@pytest.mark.django_db
def test_poem_controller_retrieve_like(mocker, poem):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}RetrievePoemsLikeService").run.return_value = poem_dict
    mocker.patch(f"{base_path}PoemByLineSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}PoemSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}render").return_value = poem_dict

    assert_responses_match(PoemController().retrieve_like(""), poem_dict)


@pytest.mark.django_db
def test_poem_controller_retrieve(mocker, poem):
    poem_dict = model_fixture_to_dict(poem)

    mocker.patch(f"{base_path}RetrievePoemService").run.return_value = poem_dict
    mocker.patch(f"{base_path}PoemByLineSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}PoemSerializer.data").return_value = poem_dict
    mocker.patch(f"{base_path}render").return_value = poem_dict

    assert_responses_match(PoemController().retrieve("", ""), poem_dict)
