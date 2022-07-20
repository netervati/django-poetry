from lib.utils import StandingData


class RetrieveAgesService:
    """
    Retrieves the list of ages.
    """

    def run(self):
        return StandingData().retrieve_ages()
