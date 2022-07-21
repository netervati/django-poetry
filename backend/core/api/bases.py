from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from api.serializers import ListSerializer, RecordSerializer
from lib.mappers import ListMapper, RecordMapper


class BaseController(ViewSet):
    def _render(self, data):
        mapper = self._mapper(data).to_dict()

        serializer = self._serializer(mapper).data

        return Response(serializer)

    def _render_list(self, data):
        mapper = self._mapper_list(data).to_dict()

        return Response(self._serializer_list(mapper).data)

    @property
    def _mapper(self):
        return RecordMapper

    @property
    def _mapper_list(self):
        return ListMapper

    @property
    def _serializer(self):
        return RecordSerializer

    @property
    def _serializer_list(self):
        return ListSerializer
