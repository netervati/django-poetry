from rest_framework.exceptions import ValidationError


from api.author.author_services import RetrieveAuthorService, RetrieveAuthorsService
from tests.fixtures import author, fake_request, user


import pytest


base_path = "api.author.author_services."


@pytest.mark.django_db
def test_retrieve_authors_service(mocker, author, fake_request):
    mocker.patch(f"{base_path}clean_params").return_value = None
    mocker.patch(f"{base_path}Validation.run").return_value = None
    mocker.patch(f"{base_path}match_like").return_value = {}
    mocker.patch(f"{base_path}Author").objects.filter.return_value = author

    subject = RetrieveAuthorsService(fake_request)

    assert subject.run() == author

    mocker.patch(f"{base_path}Validation.run").return_value = "error"

    with pytest.raises(ValidationError):
        subject.run()


@pytest.mark.django_db
def test_retrieve_author_service(mocker, author):
    mocker.patch(f"{base_path}Author").objects.get.return_value = author

    subject = RetrieveAuthorService(author.id)

    assert subject.run() == author

    mocker.patch(f"{base_path}Author").objects.get.side_effect = ValidationError

    with pytest.raises(ValidationError):
        subject.run()
