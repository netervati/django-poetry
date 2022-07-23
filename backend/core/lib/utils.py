"""
Serves as the module for utilities in the API.
"""
import yaml


def clean_params(kwargs, mapper):
    """
    Removes parameters that do not match
    the mapper attributes.
    """

    params = {}

    for key, val in kwargs.items():
        if key in mapper:
            params[key] = val

    return params


class StandingData:
    def retrieve_ages(self):
        return self.__load_yaml("ages")

    def retrieve_types(self):
        return self.__load_yaml("types")

    def __load_yaml(self, key):
        f = open(f"lib/yamls/standing_data.yml")
        data = yaml.load(f, Loader=yaml.CLoader)

        f.close()

        return self.__map(data[key])

    def __map(self, data):
        return [{"value": i} for i in data]
