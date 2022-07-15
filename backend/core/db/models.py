from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4


MAX_LENGTH = 100


class Poem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False),
    age = models.CharField(max_length=MAX_LENGTH)
    author = models.CharField(max_length=MAX_LENGTH)
    content = models.TextField()
    title = models.CharField(max_length=MAX_LENGTH)
    type = models.CharField(max_length=MAX_LENGTH)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, default=None, null=False)
