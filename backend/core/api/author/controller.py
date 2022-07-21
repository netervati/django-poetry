from django.urls import path


from api.author.services import RetrieveAuthorService, RetrieveAuthorsService
from api.bases import BaseController
from api.serializers import AuthorSerializer


class AuthorController(BaseController):
    def retrieve_list(self, request):
        result = RetrieveAuthorsService(request).run()

        return self._render_list(AuthorSerializer(result, many=True).data)

    def retrieve(self, request, id):
        result = RetrieveAuthorService(id).run()

        return self._render(AuthorSerializer(result).data)


urlpatterns = [
    path(
        "",
        AuthorController.as_view({"get": "retrieve_list"}),
        name="retrieve-authors",
    ),
    path(
        "<str:id>",
        AuthorController.as_view({"get": "retrieve"}),
        name="retrieve-author",
    ),
]
