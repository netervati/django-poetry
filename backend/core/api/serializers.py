from rest_framework import serializers


from db.models import Author, Poem


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AuthorSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Author

        fields = ["id", "name"]


class PoemByLineSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Poem

        fields = ["id", "age", "author_details", "lines", "title", "type"]


class PoemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Poem

        fields = ["id", "age", "author_details", "content", "title", "type"]


class ListSerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    data = serializers.ListField()


class RecordSerializer(serializers.Serializer):
    data = serializers.JSONField()
