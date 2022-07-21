from rest_framework.exceptions import ValidationError


from db.models import Author
from lib.mappers import ALLOWED_ATTR_FOR_AUTHOR
from lib.utils import clean_params


class RetrieveAuthorsService:
    """
    Retrieves the list of authors.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_AUTHOR)

    def run(self):
        errors = self.__validate_params()

        if errors:
            raise ValidationError(detail={"errors": errors})

        return Author.objects.filter(**self.__like_params())

    def __validate_params(self):
        errors = []

        for key, val in self.params.items():
            if not val.strip():
                errors.append({f"{key}": f"Parameter should not be blank."})

        return errors

    def __like_params(self):
        params = {}

        for key, val in self.params.items():
            params[f"{key}__icontains"] = val

        return params
