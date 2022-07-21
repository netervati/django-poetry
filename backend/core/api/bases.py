from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.serializers import ListSerializer
from lib.mappers import ListMapper


class BaseController(ViewSet):
    def _render_list(self, data):
        mapper = self._mapper(data).to_dict()

        return Response(self._serializer(mapper).data)

    @property
    def _mapper(self):
        return ListMapper

    @property
    def _serializer(self):
        return ListSerializer
