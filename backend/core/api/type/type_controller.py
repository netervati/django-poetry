from django.urls import path


from api.type.type_services import RetrieveTypesService
from api.bases import BaseController


class TypeController(BaseController):
    def retrieve(self, request):
        result = RetrieveTypesService().run()

        return self._render_list(result)


urlpatterns = [
    path(
        "",
        TypeController.as_view({"get": "retrieve"}),
        name="retrieve-types",
    ),
]
