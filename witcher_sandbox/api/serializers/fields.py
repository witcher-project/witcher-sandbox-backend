from typing import Any, Dict

from rest_framework.relations import RelatedField


class ItemSourceField(RelatedField):
    def to_representation(self, value: Any) -> Dict[str, str]:
        return {"source": value.source, "fandom_link": value.fandom_link}
