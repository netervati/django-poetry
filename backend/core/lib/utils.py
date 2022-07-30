"""
Serves as the module for utilities in the API.
"""
from api.serializers import ListSerializer, RecordSerializer
from lib.mappers import ListMapper, RecordMapper


import yaml


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
        return ListSerializer(ListMapper(data).to_dict()).data

    return RecordSerializer(RecordMapper(data).to_dict()).data


class StandingData:
    def retrieve_ages(self) -> list:
        return self.__load_yaml("ages")

    def retrieve_types(self) -> list:
        return self.__load_yaml("types")

    def __load_yaml(self, key) -> list:
        f = open(f"lib/yamls/standing_data.yml")
        data = yaml.load(f, Loader=yaml.CLoader)

        f.close()

        return self.__map(data[key])

    def __map(self, data) -> list:
        return [{"value": i} for i in data]


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
