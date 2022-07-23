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


class BaseService:
    """
    Base service for all api services.
    """

    def _validate(self, validations):
        errors = []

        if "missing_params" in validations:
            errors += self.__require_params

        if "blank_params" in validations:
            errors += self.__blank_params

        return errors

    def _like(self, params):
        new_params = {}

        for key, val in params.items():
            new_params[f"{key}__icontains"] = val

        return new_params

    @property
    def __blank_params(self):
        blank_errors = []

        for key, val in self.params.items():
            if not val.strip():
                blank_errors.append({f"{key}": f"Parameter should not be blank."})

        return blank_errors

    @property
    def __require_params(self):
        if len(self.params) == 0:
            return ["You are missing valid query parameters."]

        return []
