from lib.utils import StandingData


class RetrieveTypesService:
    """
    Retrieves the list of types.
    """

    def run(self):
        return StandingData().retrieve_types()
