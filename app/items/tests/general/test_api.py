import os
import tempfile

from django.test import TestCase
from items.models import RecipeComponent
from PIL import Image
from rest_framework import status
from rest_framework.test import APIClient

from .utils import ItemsTestManager


class ItemsAPITest(TestCase):
    """Test API request"""

    def setUp(self):
        self.client = APIClient()
        self.manager = ItemsTestManager()
        self.client.force_authenticate(self.manager.user)

    def create_test_instances(self):
        no_user_models = [RecipeComponent]
        models_map = self.manager.get_models_creation_map()

        instances = []
        for model, create in models_map.items():
            if model not in no_user_models:
                model_instance = create(self.manager.user)
            else:
                model_instance = create()
            instances.append(model_instance)

        return instances

    def test_get_items_model_list(self):
        """
        Test retrieving a list of items.
        """
        instances = self.create_test_instances()

        for instance in instances:
            url = self.manager.instance_list(instance.__class__)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIsInstance(res.data, list)

    def test_get_items_model_detail(self):
        """
        Test retrieving a single item detail.
        """
        instances = self.create_test_instances()

        for instance in instances:
            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data["id"], instance.id)

    def test_post_items_model(self):
        """
        Do POST request for each model.
        """
        instances = self.create_test_instances()

        for instance in instances:
            serialized_instance = self.manager.serialize_instance(instance)

            instance.delete()  # delete in order to prevent IDs and game_ids collison.

            res = self.client.post(
                self.manager.instance_list(instance.__class__), data=serialized_instance, format="json"
            )
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_put_items_model(self):
        """
        Test updating an item with PUT.
        """
        instances = self.create_test_instances()

        for instance in instances:
            updated_data = self.manager.serialize_instance(instance)

            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.put(url, updated_data, format="json")

            self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_items_model(self):
        """
        Test updating an item with PATCH.
        """
        instances = self.create_test_instances()

        for instance in instances:
            patch_data = {"name": "New Name"}

            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.patch(url, patch_data, format="json")

            self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_items_model(self):
        """
        Do DELETE request for each model.
        """
        instances = self.create_test_instances()

        for instance in instances:
            res = self.client.delete(self.manager.instance_detail(instance.__class__, instance.id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_craft_component_by_type(self):
        c1 = self.manager.create_crafting_component(self.manager.user, craft_type="crafting")
        c2 = self.manager.create_crafting_component(self.manager.user, craft_type="alchemy")
        c3 = self.manager.create_crafting_component(self.manager.user, craft_type="both")

        params = {"craft_type": "alchemy"}
        res = self.client.get(self.manager.instance_list(c1.__class__), params)

        self.assertNotIn(self.manager.serialize_instance(c1), res.data)
        self.assertIn(self.manager.serialize_instance(c2), res.data)
        self.assertNotIn(self.manager.serialize_instance(c3), res.data)


class ItemsImageUploadTest(TestCase):
    """Test API request"""

    def setUp(self):
        self.client = APIClient()
        self.manager = ItemsTestManager()
        self.client.force_authenticate(self.manager.user)
        self.crafting_component = self.manager.create_crafting_component(self.manager.user)

    def tearDown(self) -> None:
        self.crafting_component.img.delete()

    def test_upload_img(self):
        url = self.manager.instance_img_upload(self.crafting_component.__class__, self.crafting_component.id)
        with tempfile.NamedTemporaryFile(suffix=".png") as image_file:
            img = Image.new("RGB", (10, 10))
            img.save(image_file, format="PNG")
            image_file.seek(0)
            payload = {"img": image_file}
            res = self.client.post(url, payload, format="multipart")

        self.crafting_component.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("img", res.data)
        self.assertTrue(os.path.exists(self.crafting_component.img.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image."""
        url = self.manager.instance_img_upload(self.crafting_component.__class__, self.crafting_component.id)
        payload = {"img": "notanimage"}
        res = self.client.post(url, payload, format="multipart")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
