from django.urls import path


from api.author.author_services import RetrieveAuthorService, RetrieveAuthorsService
from api.bases import BaseController
from api.serializers import AuthorSerializer


class AuthorController(BaseController):
    def retrieve_list(self, request):
        return self._render_list(
            AuthorSerializer(RetrieveAuthorsService(request).run(), many=True).data
        )

    def retrieve(self, request, id):
        return self._render(AuthorSerializer(RetrieveAuthorService(id).run()).data)


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
