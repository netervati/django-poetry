from lib.standing_data import retrieve_standing_data


class RetrieveTypesService:
    """
    Retrieves the list of types.
    """

    def run(self):
        return retrieve_standing_data("types")
