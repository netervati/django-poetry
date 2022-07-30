from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.type.type_services import RetrieveTypesService
from lib.utils import render


class TypeController(ViewSet):
    def retrieve(self, request):
        return Response(render(RetrieveTypesService().run()))


urlpatterns = [
    path(
        "",
        TypeController.as_view({"get": "retrieve"}),
        name="retrieve-types",
    ),
]
