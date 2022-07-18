"""
Serves as the module for utilities in the API.
"""


def clean_params(kwargs, mapper):
    """
    Removes parameters that do not match
    the model attributes.
    """

    params = {}

    for key, val in kwargs.items():
        if key in mapper:
            params[key] = val

    return params
