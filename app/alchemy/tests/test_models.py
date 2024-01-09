from core.models import Tier, Type
from django.contrib.auth import get_user_model
from django.test import TestCase

from .utils import get_initial_alchemy_item_data


class AlchemyModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="test@example.com", password="testpass")
        self.tier, _ = Tier.objects.get_or_create(name="Relict", color_hex="ffffff")
        self.type, _ = Type.objects.get_or_create(name="Potion")

    def test_create_instances(self):
        """Tests creating instances of every Alchemy model."""
        alchemy_item_data = get_initial_alchemy_item_data(self.user)

        for element, model, _ in alchemy_item_data:
            self.assertEqual(str(element), element.name)
            self.assertEqual(element.user, self.user)
            self.assertEqual(element.tier.name, Tier.objects.get(id=99999).name)
            self.assertEqual(element.type.name, Type.objects.get(id=99999).name)
            self.assertEqual(element.price, 100)
            self.assertEqual(element.effect, f"Same {model.__name__.lower()} effect")
            self.assertEqual(element.source, f"Same {element.__class__.__name__.lower()} source")
            self.assertEqual(element.link, f"Same {element.__class__.__name__.lower()} link")
