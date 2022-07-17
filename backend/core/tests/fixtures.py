from db.models import Poem
from django.contrib.auth.models import User


import pytest


@pytest.fixture
def user(faker):
    return User.objects.create_user(faker.name(), faker.email(), faker.bs())


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
