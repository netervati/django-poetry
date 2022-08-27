"""
Serves as the module for the standing data
"""
import yaml


def retrieve_standing_data(key: str) -> list:
    """
    Retrieves standing data from yamls
    """
    with open(f"lib/yamls/standing_data.yml") as f:
        data = yaml.load(f, Loader=yaml.CLoader)

    map = lambda list: [{"value": i} for i in list]

    return map(data[key])
