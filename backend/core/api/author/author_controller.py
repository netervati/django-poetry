from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.author.author_services import RetrieveAuthorService, RetrieveAuthorsService
from api.serializers import AuthorSerializer
from lib.utils import render


class AuthorController(ViewSet):
    def retrieve_list(self, request):
        return Response(
            render(
                AuthorSerializer(RetrieveAuthorsService(request).run(), many=True).data
            )
        )

    def retrieve(self, request, id):
        return Response(render(AuthorSerializer(RetrieveAuthorService(id).run()).data))


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
