from api.type.type_controller import TypeController
from tests.fixtures import type
from tests.helpers import assert_responses_match


base_path = "api.type.type_controller."


def test_type_controller_retrieve(mocker, type):
    mocker.patch(f"{base_path}RetrieveTypesService.run").return_value = type
    mocker.patch(f"{base_path}render").return_value = type

    assert_responses_match(TypeController().retrieve(""), type)
