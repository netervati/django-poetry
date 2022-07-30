from lib.utils import render


class BaseService:
    """
    Base service for all api services.
    """

    def _validate(self, validations):
        errors = []

        if "missing_params" in validations:
            errors += self.__require_params

        if "blank_params" in validations:
            errors += self.__blank_params

        return errors

    def _like(self, params):
        new_params = {}

        for key, val in params.items():
            new_params[f"{key}__icontains"] = val

        return new_params

    @property
    def __blank_params(self):
        blank_errors = []

        for key, val in self.params.items():
            if not val.strip():
                blank_errors.append({f"{key}": f"Parameter should not be blank."})

        return blank_errors

    @property
    def __require_params(self):
        return (
            ["You are missing valid query parameters."] if len(self.params) == 0 else []
        )
