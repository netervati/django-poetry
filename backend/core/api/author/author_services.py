from rest_framework.exceptions import ValidationError


from api.bases import BaseService
from db.models import Author
from lib.mappers import ALLOWED_ATTR_FOR_AUTHOR
from lib.utils import clean_params


class RetrieveAuthorsService(BaseService):
    """
    Retrieves the list of authors.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_AUTHOR)

    def run(self):
        if errors := self._validate(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return Author.objects.filter(**self._like(self.params))


class RetrieveAuthorService:
    """
    Retrieves specific author.
    """

    def __init__(self, id):
        self.id = id

    def run(self):
        try:
            author = Author.objects.get(pk=self.id)
        except:
            raise ValidationError(
                detail={"errors": [f"No record with id {self.id} found."]}
            )

        return author
