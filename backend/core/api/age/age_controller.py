from django.urls import path
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.age.age_services import RetrieveAgesService
from lib.utils import render


class AgeController(ViewSet):
    def retrieve(self, request):
        return Response(render(RetrieveAgesService().run()))


urlpatterns = [
    path(
        "",
        AgeController.as_view({"get": "retrieve"}),
        name="retrieve-ages",
    ),
]
