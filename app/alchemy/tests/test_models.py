from alchemy.models import Bomb, Decotion, Oil, Potion
from core.models import Tier, Type
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.test import TestCase


class AlchemyModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="testpass"
        )
        self.tier, _ = Tier.objects.get_or_create(name="Relict", color_hex="ffffff")
        self.type, _ = Type.objects.get_or_create(name="Potion")

    def create_alchemy_instance(self, alchemy_model: Model, **params):
        default_params = {
            "user": self.user,
            "name": f"Sample {alchemy_model.__name__.lower()} name",
            "tier": self.tier,
            "type": self.type,
            "price": 100,
            "source": f"Same {alchemy_model.__name__.lower()} source",
            "link": f"Same {alchemy_model.__name__.lower()} link",
            "effect": f"Same {alchemy_model.__name__.lower()} effect",
        }
        instance_params = {**default_params, **params}
        instance = alchemy_model.objects.create(**instance_params)
        return instance

    def test_create_alchemy_instance(self):
        decotion = self.create_alchemy_instance(Decotion)
        potion = self.create_alchemy_instance(Potion)
        bomb = self.create_alchemy_instance(
            Bomb, name="Custom Bomb Name", price=150, effect="Custom Bomb Effect"
        )
        oil = self.create_alchemy_instance(Oil, source="Custom Oil Source")

        self.assertIsNotNone(decotion)
        self.assertIsNotNone(potion)
        self.assertIsNotNone(bomb)
        self.assertIsNotNone(oil)

    def test_create_decotion(self):
        decotion = self.create_alchemy_instance(
            Decotion,
            name="Test decotion 1",
            effect="Decotion's 1 effect",
            img="good_img.png",
            charges=2,
            duration_sec=3600,
            tox_points=60,
        )

        self.assertEqual(str(decotion), decotion.name)
        self.assertEqual(decotion.user, self.user)
        self.assertEqual(decotion.tier.name, self.tier.name)
        self.assertEqual(decotion.type.name, self.type.name)
        self.assertEqual(decotion.price, 100)
        self.assertEqual(decotion.effect, "Decotion's 1 effect")
        self.assertEqual(decotion.charges, 2)
        self.assertEqual(decotion.duration_sec, 3600)
        self.assertEqual(decotion.tox_points, 60)
        self.assertEqual(
            decotion.source, f"Same {decotion.__class__.__name__.lower()} source"
        )
        self.assertEqual(
            decotion.link, f"Same {decotion.__class__.__name__.lower()} link"
        )

    def test_create_potion(self):
        potion = self.create_alchemy_instance(
            Potion,
            name="Test Potion 1",
            effect="Potion's 1 effect",
            img="potion_img.png",
            charges=3,
            duration_sec=2400,
            tox_points=30,
            link="Potion's 1 link",
        )

        self.assertEqual(str(potion), potion.name)
        self.assertEqual(potion.user, self.user)
        self.assertEqual(potion.tier.name, self.tier.name)
        self.assertEqual(potion.type.name, self.type.name)
        self.assertEqual(potion.price, 100)
        self.assertEqual(potion.effect, "Potion's 1 effect")
        self.assertEqual(potion.charges, 3)
        self.assertEqual(potion.duration_sec, 2400)
        self.assertEqual(potion.tox_points, 30)
        self.assertEqual(
            potion.source, f"Same {potion.__class__.__name__.lower()} source"
        )
        self.assertEqual(potion.link, "Potion's 1 link")

    def test_create_oil(self):
        oil = self.create_alchemy_instance(
            Oil,
            name="Test Oil 1",
            effect="Oil's 1 effect",
            img="oil_img.png",
            charges=30,
            attack_bonus_perc=15,
            link="Oil's 1 link",
        )

        self.assertEqual(str(oil), oil.name)
        self.assertEqual(oil.user, self.user)
        self.assertEqual(oil.tier.name, self.tier.name)
        self.assertEqual(oil.type.name, self.type.name)
        self.assertEqual(oil.price, 100)
        self.assertEqual(oil.effect, "Oil's 1 effect")
        self.assertEqual(oil.charges, 30)
        self.assertEqual(oil.attack_bonus_perc, 15)
        self.assertEqual(oil.source, f"Same {oil.__class__.__name__.lower()} source")
        self.assertEqual(oil.link, "Oil's 1 link")

    def test_create_bomb(self):
        bomb = self.create_alchemy_instance(
            Bomb,
            name="Test Bomb 1",
            effect="Bomb's 1 effect",
            img="bomb_img.png",
            charges=3,
            duration_sec=0,
        )

        self.assertEqual(str(bomb), bomb.name)
        self.assertEqual(bomb.user, self.user)
        self.assertEqual(bomb.tier.name, self.tier.name)
        self.assertEqual(bomb.type.name, self.type.name)
        self.assertEqual(bomb.price, 100)
        self.assertEqual(bomb.effect, "Bomb's 1 effect")
        self.assertEqual(bomb.charges, 3)
        self.assertEqual(bomb.duration_sec, 0)
        self.assertEqual(bomb.source, f"Same {bomb.__class__.__name__.lower()} source")
        self.assertEqual(bomb.link, f"Same {bomb.__class__.__name__.lower()} link")

    def test_create_alchemy_element_with_default_img(self):
        instance = self.create_alchemy_instance(Potion)
        self.assertEqual(instance.img, Potion.img.field.default)
