from api.type.type_services import RetrieveTypesService
from tests.fixtures import type


base_path = "api.type.type_services."


def test_retrieve_types(mocker, type):
    mocker.patch(f"{base_path}retrieve_standing_data").return_value = [type]

    assert RetrieveTypesService().run() == [type]
