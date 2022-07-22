from django.contrib.auth.models import User
from django.db import models

import uuid


MAX_LENGTH = 100


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Poem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.CharField(max_length=MAX_LENGTH)
    author = models.CharField(max_length=MAX_LENGTH)
    content = models.TextField()
    title = models.CharField(max_length=MAX_LENGTH)
    type = models.CharField(max_length=MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    @property
    def lines(self):
        return list(filter(None, self.content.split("\n")))
