from .services import RetrievePoem


from api.serializers import PoemSerializer


from django.urls import path


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class PoemViewset(ViewSet):
    def retrieve(self, request):
        result = RetrievePoem(request).run()

        return Response(PoemSerializer(result, many=True).data)


urlpatterns = [
    path("", PoemViewset.as_view({"get": "retrieve"})),
]
