from uuid import uuid4

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .utils import (
    BOMBS_URL,
    DECOTIONS_URL,
    OILS_URL,
    POTIONS_URL,
    create_user,
    element_detail,
    get_alchemy_item_type_definitions,
    get_initial_alchemy_item_data,
)


class PublicAlchemyAPITest(TestCase):
    """Test unauthenticated API request"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="user@example.com", password="testpass")

    def test_auth_not_required(self):
        """
        Test that unauthenticated users have access to all alchemy endpoints.
        """
        for endpoint in [BOMBS_URL, DECOTIONS_URL, OILS_URL, POTIONS_URL]:
            res = self.client.get(endpoint)
            self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrive_elements(self):
        """
        Test retrieving all alchemy items from each model.
        """
        alchemy_item_types = get_alchemy_item_type_definitions()

        for url, model, serializer_class, create_function in alchemy_item_types:
            create_function(user=self.user)
            res = self.client.get(url)

            self.assertTrue(res.data)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            serializer = serializer_class(model.all().order_by("-id"), many=True)
            self.assertEqual(res.data, serializer.data)

    def test_get_element_detail(self):
        """
        Test retrieving special alchemy element by its id.
        """
        alchemy_item_data = get_initial_alchemy_item_data(self.user)

        for element, model, serializer_class in alchemy_item_data:
            url = element_detail(model, element.id)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            serializer = serializer_class(element)
            self.assertEqual(res.data, serializer.data)


class PrivateAlchemyAPITest(TestCase):
    """Test authenticated API request"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="user@example.com", password="testpass")
        self.client.force_authenticate(self.user)

    def test_post_element(self):
        """
        Test posting element for each alchemy model.
        """
        alchemy_item_types = get_alchemy_item_type_definitions()

        for url, model, serializer_class, create_function in alchemy_item_types:
            # post element for each alchemy model
            element = create_function(user=self.user, img="")
            serializer = serializer_class(element)
            model.get(pk=element.id).delete()
            res = self.client.post(url, serializer.data, format="json")

            self.assertTrue(res.data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

            element = model.get(id=res.data["id"])
            self.assertEqual(element.tier.pk, serializer.data["tier"])
            self.assertEqual(element.type.pk, serializer.data["type"])

            for key, value in serializer.data.items():
                if key in ("id"):
                    continue
                if key == "img":
                    if value is None:
                        self.assertIsNone(value)
                    else:
                        raise TypeError("Image was uploaded, fix test")
                elif key == "tier" or key == "type":
                    self.assertEqual(value, getattr(element, key).pk)
                else:
                    self.assertEqual(value, getattr(element, key))

    def test_patch_element(self):
        """
        Tests updating a special alchemy element by its id.
        """
        alchemy_item_data = get_initial_alchemy_item_data(self.user)

        for element, model, serializer_class in alchemy_item_data:
            url = element_detail(model, element.id)
            payload = {"name": f"The best {element.__class__.__name__.lower()} ever!"}
            res = self.client.patch(url, payload)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            element.refresh_from_db()
            self.assertEqual(element.name, payload["name"])

            serializer = serializer_class(element)
            self.assertEqual(res.data, serializer.data)

    def test_put_element(self):
        """
        Tests full instance update of every alchemy model.
        """
        alchemy_item_data = get_initial_alchemy_item_data(self.user)

        for element, model, serializer_class in alchemy_item_data:
            url = element_detail(model, element.id)
            payload = {
                "name": f"Put {element.__class__.__name__.lower()} name",
                "tier": element.tier.id,
                "type": element.type.id,
                "price": 9999999,
                "source": f"Put {element.__class__.__name__.lower()} source",
                "link": f"Put {element.__class__.__name__.lower()} link",
                "effect": f"Put {element.__class__.__name__.lower()} effect",
                "game_id": f"{element.__class__.__name__.lower()}_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": True,
            }
            res = self.client.put(url, payload)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            element.refresh_from_db()
            self.assertEqual(element.name, payload["name"])

            serializer = serializer_class(element)
            self.assertEqual(res.data, serializer.data)

    def test_delete_element(self):
        """
        Test deliting decotion
        """
        alchemy_item_data = get_initial_alchemy_item_data(self.user)
        for element, model, _ in alchemy_item_data:
            url = element_detail(model, element.id)
            res = self.client.delete(url)

            self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(model.objects.filter(id=element.id).exists())

    def test_user_unable_to_reassign_user(self):
        """Tests that changing the element's user results in an error."""
        new_user = create_user(email="user2@example.com", password="test123")
        alchemy_item_data = get_initial_alchemy_item_data(new_user)
        payload = {"user": new_user.id}

        for element, model, _ in alchemy_item_data:
            url = element_detail(model, element.id)
            res = self.client.patch(url, payload)
            element.refresh_from_db()

            self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
            self.assertEqual(element.user, new_user)

    def test_delete_other_user_element_error(self):
        """Tests trying to delete another user's alchemy element returns an error."""
        new_user = create_user(email="user3@example.com", password="test123")

        alchemy_item_data = get_initial_alchemy_item_data(new_user)
        for element, model, _ in alchemy_item_data:
            url = element_detail(model, element.id)
            res = self.client.delete(url)

            self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
            self.assertTrue(model.objects.filter(id=element.id).exists())

    def test_get_element_detail(self):
        """Tests retrieving a special alhemy element by its id while logged in."""
        another_user = create_user(email="another@example.com", password="testpass")
        alchemy_item_data = get_initial_alchemy_item_data(another_user)

        for element, model, serializer_class in alchemy_item_data:
            url = element_detail(model, element.id)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            serializer = serializer_class(element)
            self.assertEqual(res.data, serializer.data)
