from rest_framework.exceptions import ValidationError


from db.models import Poem
from lib.mappers import (
    ALLOWED_ATTR_FOR_POEM,
    ALLOWED_ATTR_FOR_POEM_EXACT,
    ALLOWED_ATTR_FOR_POEM_LIKE,
)
from lib.utils import clean_params, match_like, Validation


def remove_not_required(params, allowed_attributes: list) -> tuple:
    """
    Removes any non-required parameters
    before running the validation.
    """
    by_line = False
    cleaned_params = clean_params(params, allowed_attributes)

    if "by-line" in cleaned_params:
        by_line = cleaned_params["by-line"] == "true"
        cleaned_params.pop("by-line")

    return (cleaned_params, by_line)


def set_filter(params) -> dict:
    """
    Adjusts filter name for objects
    """
    if "author" in params:
        params["author__name"] = params["author"]
        params.pop("author")

    return params


class RetrievePoemsExactService:
    """
    Retrieves the poems based exactly on the query parameters.
    """

    def __init__(self, params):
        self.params, self.by_line = remove_not_required(
            params.query_params, ALLOWED_ATTR_FOR_POEM_EXACT
        )
        self.validation = Validation(self.params)

    def run(self):
        if errors := self.validation.run(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return {
            "poem": Poem.objects.filter(**set_filter(self.params)),
            "by-line": self.by_line,
        }


class RetrievePoemsLikeService:
    """
    Retrieves the poems with attributes like query parameters.
    """

    def __init__(self, params):
        self.params, self.by_line = remove_not_required(
            params.query_params, ALLOWED_ATTR_FOR_POEM_LIKE
        )
        self.validation = Validation(self.params)

    def run(self):
        if errors := self.validation.run(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return {
            "poem": Poem.objects.filter(**match_like(set_filter(self.params))),
            "by-line": self.by_line,
        }


class RetrievePoemService:
    """
    Retrieves specific poem.
    """

    def __init__(self, id, params):
        self.id = id
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM)
        self.validation = Validation(self.params)

    def run(self):
        if errors := self.validation.run(["blank_params"]):
            raise ValidationError(detail={"errors": errors})

        try:
            poem = Poem.objects.get(pk=self.id)
        except:
            raise ValidationError(
                detail={"errors": [f"No record with id {self.id} found."]}
            )

        by_line = (
            self.params["by-line"] == "true" if "by-line" in self.params else False
        )

        return {"poem": poem, "by-line": by_line}
