from django.urls import path


from api.age.age_services import RetrieveAgesService
from api.bases import BaseController


class AgeController(BaseController):
    def retrieve(self, request):
        result = RetrieveAgesService().run()

        return self._render_list(result)


urlpatterns = [
    path(
        "",
        AgeController.as_view({"get": "retrieve"}),
        name="retrieve-ages",
    ),
]
