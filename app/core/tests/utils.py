from core.models import Tier, Type
from django.contrib.auth import get_user_model


class CoreTestManager:
    def __init__(self) -> None:
        self.default_tier = self.get_or_create_tier(id=99999, name="Test Tier", color_hex="ffffff")[0]
        self.default_type = self.get_or_create_type(id=99999, name="Test Type")[0]

    @staticmethod
    def create_user(**params) -> get_user_model():
        """Create a new user instance."""
        return get_user_model().objects.create(**params)

    @staticmethod
    def get_or_create_tier(**params) -> Tier:
        """Create or get an existing Tier instance."""
        return Tier.objects.get_or_create(**params)

    @staticmethod
    def get_or_create_type(**params) -> Type:
        """Create or get an existing Type instance."""
        return Type.objects.get_or_create(**params)
