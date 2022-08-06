from api.age.age_controller import AgeController
from tests.fixtures import age
from tests.helpers import assert_responses_match


base_path = "api.age.age_controller."


def test_age_controller_retrieve(mocker, age):
    mocker.patch(f"{base_path}RetrieveAgesService.run").return_value = age
    mocker.patch("api.age.age_controller.render").return_value = age

    assert_responses_match(AgeController().retrieve(""), age)
