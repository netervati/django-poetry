from db.models import Poem


from rest_framework.exceptions import ValidationError


class RetrievePoemsExactService:
    def __init__(self, params):
        self.params = params.query_params

    def run(self):
        self.__clean_params()
        errors = self.__validate_params()

        if errors:
            raise ValidationError(detail={"errors": errors})

        return Poem.objects.filter(**self.params)

    def __clean_params(self):
        params = {}

        for key, val in self.params.items():
            if key in Poem().__dict__:
                params[key] = val

        self.params = params

    # TO-DO feat_v1.0002: Create validation layer
    def __validate_params(self):
        errors = []
        if len(self.params) == 0:
            errors.append("You are missing valid query parameters.")

        for key, val in self.params.items():
            if not val.strip():
                errors.append({f"{key}": f"Parameter should not be blank."})

        return errors
