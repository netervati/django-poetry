"""
Serves as the module for the standing data
"""
import yaml


def map_standing_data(data: list) -> list:
    return [{"value": i} for i in data]


def retrieve_standing_data(key: str) -> list:
    with open(f"lib/yamls/standing_data.yml") as f:
        data = yaml.load(f, Loader=yaml.CLoader)

    return map_standing_data(data[key])
