from django.contrib.auth.models import User
from django.db import models

import uuid


MAX_LENGTH = 100


class Author(models.Model):
    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=MAX_LENGTH
    )
    name = models.CharField(max_length=MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Poem(models.Model):
    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=MAX_LENGTH
    )
    age = models.CharField(max_length=MAX_LENGTH)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=MAX_LENGTH)
    type = models.CharField(max_length=MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    @property
    def author_details(self):
        return {"id": self.author.id, "name": self.author.name}

    @property
    def lines(self):
        return list(filter(None, self.content.split("\n")))
