from django.contrib.auth.models import User


from db.models import Age, Author, Poem, Type


import pytest


@pytest.fixture
def user(faker):
    return User.objects.create_user(faker.name(), faker.email(), faker.bs())


@pytest.fixture
def age(user, faker):
    return Age.objects.create(
        name=faker.company_suffix(),
        user=user,
    )


@pytest.fixture
def author(user, faker):
    return Author.objects.create(
        name=faker.name(),
        user=user,
    )


@pytest.fixture
def poem(user, faker):
    return Poem.objects.create(
        age=faker.company_suffix(),
        author=faker.name(),
        content=faker.text(),
        title=faker.catch_phrase(),
        type=faker.company_suffix(),
        user=user,
    )


@pytest.fixture
def type(user, faker):
    return Type.objects.create(
        name=faker.company_suffix(),
        user=user,
    )
