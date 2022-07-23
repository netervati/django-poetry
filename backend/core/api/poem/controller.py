from django.urls import path


from api.bases import BaseController
from api.poem.services import (
    RetrievePoemService,
    RetrievePoemsExactService,
    RetrievePoemsLikeService,
)
from api.serializers import PoemByLineSerializer, PoemSerializer


class PoemController(BaseController):
    def retrieve_exact(self, request):
        return self._render_list(
            self.__poem_serialized(RetrievePoemsExactService(request).run(), many=True)
        )

    def retrieve_like(self, request):
        return self._render_list(
            self.__poem_serialized(RetrievePoemsLikeService(request).run(), many=True)
        )

    def retrieve(self, request, id):
        return self._render(
            self.__poem_serialized(RetrievePoemService(id, request).run())
        )

    def __poem_serialized(self, result, many=False):
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
