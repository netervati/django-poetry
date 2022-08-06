from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.forms import model_to_dict
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


import json


def assert_attributes_present(attribute_list, param):
    for i in attribute_list:
        assert i in param


def assert_attributes_not_present(attribute_list, param):
    for i in attribute_list:
        assert i not in param


def assert_responses_match(a, b):
    assert to_response(a) == to_response(b)


def to_response(subject):
    subject = subject if isinstance(subject, Response) else Response(subject)
    subject.accepted_renderer = JSONRenderer()
    subject.accepted_media_type = "application/json"
    subject.renderer_context = {}
    subject.render()

    return subject.rendered_content


def model_fixture_to_dict(model):
    return json.dumps(model, cls=ExtendedEncoder)


class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)
