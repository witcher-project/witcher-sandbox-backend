from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .utils import AlchemyTestManager


class PrivateAclhemyAPITest(TestCase):
    """Test authenticated API request"""

    def setUp(self):
        self.client = APIClient()
        self.manager = AlchemyTestManager()
        self.client.force_authenticate(self.manager.user)

    def create_test_instances(self):
        models_map = self.manager.get_models_creation_map()

        instances = []

        for _, create in models_map.items():
            model_instance = create(self.manager.user)
            instances.append(model_instance)

        return instances

    def test_get_alchemy_model_list(self):
        """
        Test retrieving a list of items.
        """
        instances = self.create_test_instances()

        for instance in instances:
            url = self.manager.instance_list(instance.__class__)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIsInstance(res.data, list)

    def test_get_alchemy_model_detail(self):
        """
        Test retrieving a single item detail.
        """
        instances = self.create_test_instances()

        for instance in instances:
            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.get(url)

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data["id"], instance.id)

    def test_post_alchemy_model(self):
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

    def test_put_alchemy_model(self):
        """
        Test updating an item with PUT.
        """
        instances = self.create_test_instances()

        for instance in instances:
            updated_data = self.manager.serialize_instance(instance)

            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.put(url, updated_data, format="json")

            self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_alchemy_model(self):
        """
        Test updating an item with PATCH.
        """
        instances = self.create_test_instances()

        for instance in instances:
            patch_data = {"name": "New Name"}

            url = self.manager.instance_detail(instance.__class__, instance.id)
            res = self.client.patch(url, patch_data, format="json")

            self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_alchemy_model(self):
        """
        Do DELETE request for each model.
        """
        instances = self.create_test_instances()

        for instance in instances:
            res = self.client.delete(self.manager.instance_detail(instance.__class__, instance.id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
