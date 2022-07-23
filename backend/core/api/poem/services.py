from rest_framework.exceptions import ValidationError


from api.bases import BaseService
from db.models import Poem
from lib.mappers import (
    ALLOWED_ATTR_FOR_POEM,
    ALLOWED_ATTR_FOR_POEM_EXACT,
    ALLOWED_ATTR_FOR_POEM_LIKE,
)
from lib.utils import clean_params


class RetrievePoemsExactService(BaseService):
    """
    Retrieves the poems based exactly on the query parameters.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM_EXACT)

    def run(self):
        if errors := self._validate_params(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return Poem.objects.filter(**self.params)


class RetrievePoemsLikeService(BaseService):
    """
    Retrieves the poems with attributes like query parameters.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM_LIKE)

    def run(self):
        if errors := self._validate_params(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return Poem.objects.filter(**self.__like_params)

    @property
    def __like_params(self):
        params = {}

        for key, val in self.params.items():
            params[f"{key}__icontains"] = val

        return params


class RetrievePoemService(BaseService):
    """
    Retrieves specific poem.
    """

    def __init__(self, id, params):
        self.id = id
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM)

    def run(self):
        if errors := self._validate_params(["blank_params"]):
            raise ValidationError(detail={"errors": errors})

        by_line = (
            self.params["by-line"] == "true" if "by-line" in self.params else False
        )

        try:
            poem = Poem.objects.get(pk=self.id)
        except:
            raise ValidationError(
                detail={"errors": [f"No record with id {self.id} found."]}
            )

        return {"poem": poem, "by-line": by_line}
