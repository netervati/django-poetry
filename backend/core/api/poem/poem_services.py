from rest_framework.exceptions import ValidationError


from api.bases import BaseService
from db.models import Poem
from lib.mappers import (
    ALLOWED_ATTR_FOR_POEM,
    ALLOWED_ATTR_FOR_POEM_EXACT,
    ALLOWED_ATTR_FOR_POEM_LIKE,
)
from lib.utils import clean_params


class ListPoemService(BaseService):
    def _clean(self, params, allowed_attributes):
        by_line = False

        cleaned_params = clean_params(params, allowed_attributes)

        if "by-line" in cleaned_params:
            by_line = cleaned_params["by-line"] == "true"
            cleaned_params.pop("by-line")

        return (cleaned_params, by_line)

    def _fix_filters(self, params):
        if "author" in params:
            params["author__name"] = params["author"]
            params.pop("author")

        return params


class RetrievePoemsExactService(ListPoemService):
    """
    Retrieves the poems based exactly on the query parameters.
    """

    def __init__(self, params):
        self.params, self.by_line = self._clean(
            params.query_params, ALLOWED_ATTR_FOR_POEM_EXACT
        )

    def run(self):
        if errors := self._validate(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        self.params = self._fix_filters(self.params)

        return {"poem": Poem.objects.filter(**self.params), "by-line": self.by_line}


class RetrievePoemsLikeService(ListPoemService):
    """
    Retrieves the poems with attributes like query parameters.
    """

    def __init__(self, params):
        self.params, self.by_line = self._clean(
            params.query_params, ALLOWED_ATTR_FOR_POEM_LIKE
        )

    def run(self):
        if errors := self._validate(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        self.params = self._fix_filters(self.params)

        return {
            "poem": Poem.objects.filter(**self._like(self.params)),
            "by-line": self.by_line,
        }


class RetrievePoemService(BaseService):
    """
    Retrieves specific poem.
    """

    def __init__(self, id, params):
        self.id = id
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM)

    def run(self):
        if errors := self._validate(["blank_params"]):
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
