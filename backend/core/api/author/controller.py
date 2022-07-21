from django.urls import path


from api.author.services import RetrieveAuthorsService
from api.defaults import BaseController
from api.serializers import AuthorSerializer


class AuthorController(BaseController):
    def retrieve(self, request):
        result = RetrieveAuthorsService(request).run()

        return self._render_list(AuthorSerializer(result, many=True).data)


urlpatterns = [
    path(
        "",
        AuthorController.as_view({"get": "retrieve"}),
        name="retrieve-authors",
    ),
]
