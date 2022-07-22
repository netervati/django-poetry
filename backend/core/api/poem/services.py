from rest_framework.exceptions import ValidationError


from db.models import Poem
from lib.mappers import ALLOWED_ATTR_FOR_POEM_EXACT, ALLOWED_ATTR_FOR_POEM_LIKE
from lib.utils import clean_params


class RetrievePoemsExactService:
    """
    Retrieves the poems based exactly on the query parameters.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM_EXACT)

    def run(self):
        errors = self.__validate_params()

        if errors:
            raise ValidationError(detail={"errors": errors})

        return Poem.objects.filter(**self.params)

    # TO-DO feat_v1.0002: Create validation layer
    def __validate_params(self):
        errors = []
        if len(self.params) == 0:
            errors.append("You are missing valid query parameters.")

        for key, val in self.params.items():
            if not val.strip():
                errors.append({f"{key}": f"Parameter should not be blank."})

        return errors


class RetrievePoemsLikeService:
    """
    Retrieves the poems with attributes like query parameters.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_POEM_LIKE)

    def run(self):
        errors = self.__validate_params()

        if errors:
            raise ValidationError(detail={"errors": errors})

        return Poem.objects.filter(**self.__like_params())

    def __validate_params(self):
        errors = []
        if len(self.params) == 0:
            errors.append("You are missing valid query parameters.")

        for key, val in self.params.items():
            if not val.strip():
                errors.append({f"{key}": f"Parameter should not be blank."})

        return errors

    def __like_params(self):
        params = {}

        for key, val in self.params.items():
            params[f"{key}__icontains"] = val

        return params


class RetrievePoemService:
    """
    Retrieves specific poem.
    """

    def __init__(self, id, params):
        self.id = id
        self.params = params.query_params

    def run(self):
        errors = self.__validate_params()

        by_line = (
            self.params["by-line"] == "true" if "by-line" in self.params else False
        )

        if errors:
            raise ValidationError(detail={"errors": errors})

        try:
            poem = Poem.objects.get(pk=self.id)
        except:
            raise ValidationError(
                detail={"errors": f"No record with id {self.id} found."}
            )

        return {"poem": poem, "by-line": bool(by_line)}

    def __validate_params(self):
        errors = []

        for key, val in self.params.items():
            if not val.strip():
                errors.append({f"{key}": f"Parameter should not be blank."})

        return errors
