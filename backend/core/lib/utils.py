def clean_params(kwargs, model):
    """
    Removes parameters that do not match
    the model attributes.
    """

    params = {}

    for key, val in kwargs.items():
        if key in model().__dict__:
            if (
                key != "id"
                and key != "created_at"
                and key != "updated_at"
                and key != "user_id"
            ):
                params[key] = val

    return params
