from alchemy.models import Bomb, Decotion, Oil, Potion
from alchemy.serializers import (
    BombSerializer,
    DecotionSerializer,
    OilSerializer,
    PotionSerializer,
)
from core.models import Tier, Type
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

DECOTIONS_URL = reverse('alchemy:decotion-list')
POTIONS_URL = reverse('alchemy:potion-list')
OILS_URL = reverse('alchemy:oil-list')
BOMBS_URL = reverse('alchemy:bomb-list')


def create_alchemy_element(user, alchemy_model, **params):
    defaults = {
        "user": user,
        "name": f'Sample {alchemy_model.__name__.lower()} name',
        "img": '',
        "tier": f'Sample {alchemy_model.__name__.lower()} tier',
        "type": f'Sample {alchemy_model.__name__.lower()} type',
        "price": 100,
        "source": f'Same {alchemy_model.__name__.lower()} source',
        "link": 'witcherfandom',
        "effect": f'Same {alchemy_model.__name__.lower()} effect',
    }
    defaults.update(params)

    tier, _ = Tier.objects.get_or_create(name=defaults['tier'], color_hex="ffffff")
    type, _ = Type.objects.get_or_create(name=defaults['type'])

    defaults['tier'] = tier
    defaults['type'] = type

    alchemy_element = alchemy_model.objects.create(**defaults)
    return alchemy_element


def create_decotion(user, **params):
    return create_alchemy_element(user, Decotion, **params)


def create_potion(user, **params):
    return create_alchemy_element(user, Potion, **params)


def create_oil(user, **params):
    return create_alchemy_element(user, Oil, **params)


def create_bomb(user, **params):
    return create_alchemy_element(user, Bomb, **params)


class PublicAlchemyAPITest(TestCase):
    """Test unauthenticated API request"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass'
        )

    def test_auth_not_required(self):
        res = self.client.get(DECOTIONS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrive_decotions(self):
        """Test retrieving all decotions items"""
        create_decotion(user=self.user)
        create_decotion(user=self.user)

        res = self.client.get(DECOTIONS_URL)

        decotions = Decotion.objects.all().order_by('-id')
        serializer = DecotionSerializer(decotions, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_potions(self):
        """Test retrieving all potions items"""
        create_potion(user=self.user)
        create_potion(user=self.user)

        res = self.client.get(POTIONS_URL)

        potions = Potion.objects.all().order_by('-id')
        serializer = PotionSerializer(potions, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_oils(self):
        """Test retrieving all oils items"""
        create_oil(user=self.user)
        create_oil(user=self.user)

        res = self.client.get(OILS_URL)

        oils = Oil.objects.all().order_by('-id')
        serializer = OilSerializer(oils, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_bombs(self):
        """Test retrieving all bombs items"""
        create_bomb(user=self.user)
        create_bomb(user=self.user)

        res = self.client.get(BOMBS_URL)

        bombs = Bomb.objects.all().order_by('-id')
        serializer = BombSerializer(bombs, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateAlchemyAPITest(TestCase):
    """Test authenticated API request"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_delete_decotion(self):
        pass
