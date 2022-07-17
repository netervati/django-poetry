"""
Retrieves the poems based exactly on the query parameters.
"""
from rest_framework.exceptions import ValidationError


from db.models import Poem
from lib.utils import clean_params


class RetrievePoemsExactService:
    def __init__(self, params):
        self.params = clean_params(params.query_params, Poem)

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
