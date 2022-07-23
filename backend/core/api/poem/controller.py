from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.bases import BaseController
from api.poem.services import (
    RetrievePoemService,
    RetrievePoemsExactService,
    RetrievePoemsLikeService,
)
from api.serializers import PoemByLineSerializer, PoemSerializer


class PoemController(BaseController):
    def retrieve_exact(self, request):
        result = RetrievePoemsExactService(request).run()

        return self._render_list(PoemSerializer(result, many=True).data)

    def retrieve_like(self, request):
        result = RetrievePoemsLikeService(request).run()

        return self._render_list(PoemSerializer(result, many=True).data)

    def retrieve(self, request, id):
        result = RetrievePoemService(id, request).run()

        serializer = (
            PoemByLineSerializer if result["by-line"] is True else PoemSerializer
        )

        return self._render(serializer(result["poem"]).data)


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
