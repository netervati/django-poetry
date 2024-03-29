from django.contrib.auth.models import User


from db.models import Author, Poem


import pytest


@pytest.fixture
def user(faker):
    return User.objects.create_user(faker.name(), faker.email(), faker.bs())


@pytest.fixture
def age(faker):
    return {"value": faker.company_suffix()}


@pytest.fixture
def author(user, faker):
    return Author.objects.create(
        name=faker.name(),
        user=user,
    )


@pytest.fixture
def poem(author, user, faker):
    return Poem.objects.create(
        age=faker.company_suffix(),
        author=author,
        content=faker.text(),
        title=faker.catch_phrase(),
        type=faker.company_suffix(),
        user=user,
    )


@pytest.fixture
def type(faker):
    return {"value": faker.catch_phrase()}


@pytest.fixture
def fake_request():
    return FakeRequest


class FakeRequest:
    @property
    def query_params():
        return
