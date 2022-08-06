from api.age.age_services import RetrieveAgesService
from tests.fixtures import age


base_path = "api.age.age_services."


def test_retrieve_ages(mocker, age):
    mocker.patch(f"{base_path}retrieve_standing_data").return_value = age

    assert RetrieveAgesService().run() == age
