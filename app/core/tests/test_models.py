from core.models import Tier, Type
from django.test import TestCase


class ModelTest(TestCase):
    """Test models"""
    def test_create_tier(self):
        """Test creating a Tier"""
        tier = Tier.objects.create(name="Relict", color_hex="FF0000")
        self.assertEqual(tier.name, "Relict")
        self.assertEqual(tier.color_hex, "FF0000")

    def test_create_type(self):
        """Test creating a Type"""
        type = Type.objects.create(name="Potion")
        self.assertEqual(type.name, "Potion")

    def test_tier_hexcolor_length_too_big(self):
        """Test the length of the color_hex field in the Tier model is too big"""
        tier = Tier.objects.create(name="Relict", color_hex="FF0000")
        self.assertEqual(len(tier.color_hex), 6)
