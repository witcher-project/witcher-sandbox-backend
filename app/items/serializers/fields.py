from rest_framework.serializers import RelatedField


class SourceField(RelatedField):
    def to_representation(self, value):
        return {"source": value.source, "link": value.link}
