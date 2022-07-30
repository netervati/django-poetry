from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.poem.poem_services import (
    RetrievePoemService,
    RetrievePoemsExactService,
    RetrievePoemsLikeService,
)
from api.serializers import PoemByLineSerializer, PoemSerializer
from lib.utils import render


class PoemController(ViewSet):
    def retrieve_exact(self, request):
        return Response(
            render(
                self.__serialize(RetrievePoemsExactService(request).run(), many=True)
            )
        )

    def retrieve_like(self, request):
        return Response(
            render(self.__serialize(RetrievePoemsLikeService(request).run(), many=True))
        )

    def retrieve(self, request, id):
        return Response(
            render(self.__serialize(RetrievePoemService(id, request).run()))
        )

    def __serialize(self, result, many=False):
        serializer = (
            PoemByLineSerializer if result["by-line"] is True else PoemSerializer
        )

        return serializer(result["poem"], many=many).data


urlpatterns = [
    path(
        "<str:id>",
        PoemController.as_view({"get": "retrieve"}),
        name="retrieve-poem",
    ),
    path(
        "exact/",
        PoemController.as_view({"get": "retrieve_exact"}),
        name="retrieve-poems-exact",
    ),
    path(
        "like/",
        PoemController.as_view({"get": "retrieve_like"}),
        name="retrieve-poems-like",
    ),
]
