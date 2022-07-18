from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.poem.services import RetrievePoemsExactService, RetrievePoemsLikeService
from api.serializers import PoemSerializer


class PoemController(ViewSet):
    def retrieve_exact(self, request):
        result = RetrievePoemsExactService(request).run()

        return Response(PoemSerializer(result, many=True).data)

    def retrieve_like(self, request):
        result = RetrievePoemsLikeService(request).run()

        return Response(PoemSerializer(result, many=True).data)


urlpatterns = [
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
