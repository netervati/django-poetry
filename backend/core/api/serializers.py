from rest_framework import serializers


from db.models import Age, Author, Poem, Type


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)

            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AgeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Age

        fields = ["name"]


class AuthorSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Author

        fields = ["name"]


class PoemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Poem

        fields = ["age", "author", "content", "title", "type"]


class TypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Type

        fields = ["name"]
