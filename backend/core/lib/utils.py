def clean_params(kwargs, model):
    """
    Removes parameters that do not match
    the model attributes.
    """

    params = {}

    for key, val in kwargs.items():
        if key in model().__dict__:
            params[key] = val

    return params
