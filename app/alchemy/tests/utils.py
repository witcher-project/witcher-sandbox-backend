from uuid import uuid4

from alchemy.models import BaseAlchemyElement, Bomb, Decotion, Oil, Potion
from alchemy.serializers import (
    BombSerializer,
    DecotionSerializer,
    OilSerializer,
    PotionSerializer,
)
from core.models import Tier, Type
from django.contrib.auth import get_user_model
from django.urls import reverse

# URLs for alchemy endpoints
DECOTIONS_URL = reverse("alchemy:decotion-list")
POTIONS_URL = reverse("alchemy:potion-list")
OILS_URL = reverse("alchemy:oil-list")
BOMBS_URL = reverse("alchemy:bomb-list")


def element_list(model: type) -> str:
    """Generate the URL for listing elements of a specific model."""
    return reverse(f"alchemy:{model.__name__.lower()}-list")


def element_detail(model: type, id: int) -> str:
    """Generate the URL for retrieving details of an element of a specific model by its ID."""
    return reverse(f"alchemy:{model.__name__.lower()}-detail", args=[id])


def create_tier(**params) -> Tier:
    """Create or get an existing Tier instance."""
    return Tier.objects.get_or_create(**params)


def create_type(**params) -> Type:
    """Create or get an existing Type instance."""
    return Type.objects.get_or_create(**params)


def create_user(**params) -> get_user_model():
    """Create a new user instance."""
    return get_user_model().objects.create(**params)


def create_decotion(user, **params) -> Decotion:
    """Create a new Decotion instance."""
    return create_alchemy_element(user, Decotion, **params)


def create_potion(user, **params) -> Potion:
    """Create a new Potion instance."""
    return create_alchemy_element(user, Potion, **params)


def create_oil(user, **params) -> Oil:
    """Create a new Oil instance."""
    return create_alchemy_element(user, Oil, **params)


def create_bomb(user, **params) -> Bomb:
    """Create a new Bomb instance."""
    return create_alchemy_element(user, Bomb, **params)


def create_alchemy_element(user: get_user_model(), alchemy_model: type, **params) -> BaseAlchemyElement:
    """
    Create a new instance of an alchemy element.

    Args:
        user: The user associated with the alchemy element.
        alchemy_model: The specific alchemy model (Decotion, Potion, Oil, or Bomb).
        params: Additional parameters for creating the alchemy element.

    Returns:
        The created alchemy element instance.
    """
    defaults = {
        "user": user,
        "name": f"Sample {alchemy_model.__name__.lower()} name",
        "img": None,  # temporary exclude default img
        "tier": create_tier(id=99999, name="Test Tier", color_hex="ffffff")[0],
        "type": create_type(id=99999, name="Test Type")[0],
        "price": 100,
        "source": f"Same {alchemy_model.__name__.lower()} source",
        "link": f"Same {alchemy_model.__name__.lower()} link",
        "effect": f"Same {alchemy_model.__name__.lower()} effect",
        "game_id": f"{alchemy_model.__name__.lower()}_{str(uuid4())[:8]}",
        "craftable": True,
        "dismantlable": True,
    }

    defaults.update(params)
    alchemy_element = alchemy_model.objects.create(**defaults)
    return alchemy_element


def get_alchemy_item_type_definitions() -> list:
    """
    Get the definitions for different alchemy item types.

    Returns:
        List: A list of tuples containing URL, model, serializer, and creation function for each alchemy item type.
    """
    return [
        (DECOTIONS_URL, Decotion.objects, DecotionSerializer, create_decotion),
        (POTIONS_URL, Potion.objects, PotionSerializer, create_potion),
        (OILS_URL, Oil.objects, OilSerializer, create_oil),
        (BOMBS_URL, Bomb.objects, BombSerializer, create_bomb),
    ]


def get_initial_alchemy_item_data(user) -> list:
    """
    Get the initial data for alchemy items.

    Args:
        user: The user for whom the initial alchemy items are created.

    Returns:
        List: A list of tuples containing initial data, model, and serializer for each alchemy item.
    """
    return [
        (create_decotion(user), Decotion, DecotionSerializer),
        (create_potion(user), Potion, PotionSerializer),
        (create_oil(user), Oil, OilSerializer),
        (create_bomb(user), Bomb, BombSerializer),
    ]
