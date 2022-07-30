"""
Serves as the module for utilities in the API.
"""
from api.serializers import ListSerializer, RecordSerializer


def clean_params(kwargs: dict, mapper: list) -> dict:
    """
    Removes parameters that do not match
    the mapper attributes.
    """
    params = {}

    for key, val in kwargs.items():
        if key in mapper:
            params[key] = val

    return params


def map_data(data, list=False):
    """
    Maps the API service results
    """
    base = {"total_records": 0, "attributes": data}

    if list is False:
        base.pop("total_records")
    else:
        base["total_records"] = len(data)

    return base


def match_like(params):
    """
    Applies LIKE SQL operator to params
    """
    new_params = {}

    for key, val in params.items():
        new_params[f"{key}__icontains"] = val

    return new_params


def render(data):
    """
    Formats API service results
    """
    if isinstance(data, list):
        return ListSerializer(map_data(data, list=True)).data

    return RecordSerializer(map_data(data)).data


class Validation:
    """
    Handles validation of params in services
    """

    def __init__(self, params):
        self.params = params

    def run(self, validations):
        errors = []

        for i in validations:
            errors.extend(getattr(self, f"_{i}"))

        return errors

    @property
    def _blank_params(self):
        blank_errors = []

        for key, val in self.params.items():
            if not val.strip():
                blank_errors.append({f"{key}": f"Parameter should not be blank."})

        return blank_errors

    @property
    def _missing_params(self):
        return (
            ["You are missing valid query parameters."] if len(self.params) == 0 else []
        )
