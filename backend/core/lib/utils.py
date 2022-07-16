"""
Removes parameters that do not match the model attributes.
"""
def clean_params(kwargs, model):
    params = {}

    for key, val in kwargs.items():
        if key in model().__dict__:
            params[key] = val

    return params
