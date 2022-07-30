from rest_framework.exceptions import ValidationError


from db.models import Author
from lib.mappers import ALLOWED_ATTR_FOR_AUTHOR
from lib.utils import clean_params, match_like, Validation


class RetrieveAuthorsService:
    """
    Retrieves the list of authors.
    """

    def __init__(self, params):
        self.params = clean_params(params.query_params, ALLOWED_ATTR_FOR_AUTHOR)
        self.validation = Validation(self.params)

    def run(self):
        if errors := self.validation.run(["missing_params", "blank_params"]):
            raise ValidationError(detail={"errors": errors})

        return Author.objects.filter(**match_like(self.params))


class RetrieveAuthorService:
    """
    Retrieves specific author based on ID.
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
