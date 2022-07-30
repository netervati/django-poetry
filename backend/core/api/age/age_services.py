from lib.standing_data import retrieve_standing_data


class RetrieveAgesService:
    """
    Retrieves the list of ages.
    """

    def run(self):
        return retrieve_standing_data("ages")
