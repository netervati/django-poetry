from api.author.author_controller import AuthorController
from tests.fixtures import author, user
from tests.helpers import assert_responses_match, model_fixture_to_dict


import pytest


base_path = "api.author.author_controller."


@pytest.mark.django_db
def test_age_controller_retrieve_list(mocker, author):
    author_dict = model_fixture_to_dict(author)

    mocker.patch(f"{base_path}RetrieveAuthorsService").run.return_value = author_dict
    mocker.patch(f"{base_path}AuthorSerializer.data").return_value = author_dict
    mocker.patch(f"{base_path}render").return_value = author_dict

    assert_responses_match(AuthorController().retrieve_list(""), author_dict)


@pytest.mark.django_db
def test_age_controller_retrieve(mocker, author):
    author_dict = model_fixture_to_dict(author)

    mocker.patch(f"{base_path}RetrieveAuthorService").run.return_value = author_dict
    mocker.patch(f"{base_path}AuthorSerializer.data").return_value = author_dict
    mocker.patch(f"{base_path}render").return_value = author_dict

    assert_responses_match(AuthorController().retrieve("", ""), author_dict)
