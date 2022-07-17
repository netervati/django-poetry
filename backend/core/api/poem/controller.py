from .services import RetrievePoemsExactService


from api.serializers import PoemSerializer


from django.urls import path


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class PoemController(ViewSet):
    def retrieve(self, request):
        result = RetrievePoemsExactService(request).run()

        return Response(PoemSerializer(result, many=True).data)


urlpatterns = [
    path("", PoemController.as_view({"get": "retrieve"}), name="get-poems"),
]
