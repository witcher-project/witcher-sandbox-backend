from uuid import uuid4

from core.tests.utils import CoreTestManager
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.urls import reverse

from ...models.alchemy_models import Bomb, Oil, Potion
from ...serializers.alchemy_serializers import model_serializer_mapping


class AlchemyTestManager:
    """
    Test manager for the Alchemy app.

    This class provides methods to create and manage instances of alchemy-related models
    like Bomb, Oil, and Potion. It includes functionalities for instance creation,
    serialization, and URL generation for these models.

    Attributes:
        core_manager (CoreTestManager): An instance of CoreTestManager for core functionalities.
        user (User): A user instance created for testing purposes.
    """

    def __init__(self) -> None:
        self.core_manager = CoreTestManager()
        self.user = self.core_manager.create_user(email="alchemy.test.user@example.com", password="testpass")

    def instance_list(self, model: Model) -> str:
        """
        Generate the URL for listing instances of a specific model.

        Args:
            model (Model): The Django model class for which to generate the list URL.

        Returns:
            str: The URL for listing instances of the specified model.

        Raises:
            ValueError: If the provided model is not recognized.
        """

        model_to_url = {
            Bomb: "items:alchemy:bombs-list",
            Oil: "items:alchemy:oils-list",
            Potion: "items:alchemy:potions-list",
        }
        try:
            return reverse(model_to_url[model])
        except KeyError:
            raise ValueError(f"Unknown model: {model}")

    @staticmethod
    def instance_detail(model: type, id: int) -> str:
        """
        Generate the URL for retrieving details of an instance of a specific model by its ID.

        Args:
            model (type): The Django model class for which to generate the detail URL.
            id (int): The ID of the instance for which to generate the URL.

        Returns:
            str: The URL for retrieving details of the specified model instance.

        Raises:
            ValueError: If the provided model is not recognized.
        """

        model_to_url = {
            Bomb: "items:alchemy:bombs-detail",
            Oil: "items:alchemy:oils-detail",
            Potion: "items:alchemy:potions-detail",
        }
        try:
            return reverse(model_to_url[model], args=[id])
        except KeyError:
            raise ValueError(f"Unknown model: {model}")

    def create_potion(self, user, **params) -> Potion:
        """Create a new Potion instance."""
        return self._create_instance(user, Potion, **params)

    def create_oil(self, user, **params) -> Oil:
        """Create a new Oil instance."""
        return self._create_instance(user, Oil, **params)

    def create_bomb(self, user, **params) -> Bomb:
        """Create a new Bomb instance."""
        return self._create_instance(user, Bomb, **params)

    def _create_instance(self, user: get_user_model(), model: Model, **params: dict):
        """
        Private method to create an instance of a given model with specified parameters.

        This method is used internally to create instances of models with default and additional parameters.

        Args:
            user (User): The user associated with the model instance.
            model (Model): The Django model class for the instance.
            **params (dict): Additional parameters for the instance.

        Returns:
            An instance of the specified model.
        """

        # private in order to avoid unexcpected model for which we don't have a payload
        payload = self.get_default_model_payload(model)
        payload.update(**params)
        instance = model.objects.create(user=user, **payload)
        return instance

    def serialize_instance(self, instance):
        """
        Serialize a model instance using the appropriate serializer.

        This method finds the correct serializer for a given model instance from the model_serializer_map
        and then returns the serialized data.

        Args:
            instance (Model instance): The instance to be serialized.

        Returns:
            dict: The serialized data of the instance.
        """

        serializer_class = model_serializer_mapping[type(instance)]
        serializer = serializer_class(instance=instance)
        return serializer.data

    def get_default_model_payload(self, model: Model) -> dict:
        """
        Get the default payload for creating an instance of a specific model.

        This method returns a set of default values for creating instances of various models
        in the Alchemy app.

        Args:
            model (Model): The Django model class for which to generate the default payload.

        Returns:
            dict: A dictionary containing default values for the model instance.

        Raises:
            ValueError: If the model is not supported or recognized.
        """
        if model == Bomb:
            return {
                "name": "Test bomb",
                "description": "Test Bomb description",
                "img": None,
                "tier": self.core_manager.default_tier,
                "type": self.core_manager.default_type,
                "price": 777,
                "link": "Test bomb link",
                "game_id": f"test_bomb_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": False,
                "charges": 3,
                "duration_sec": 10,
            }
        elif model == Oil:
            return {
                "name": "Test Oil",
                "description": "Test Oil description",
                "img": None,
                "tier": self.core_manager.default_tier,
                "type": self.core_manager.default_type,
                "price": 777,
                "link": "Test Oil link",
                "game_id": f"test_oil_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": False,
                "charges": 30,
                "attack_bonus_perc": 15,
            }
        elif model == Potion:
            return {
                "name": "Test Potion",
                "description": "Test Potion description",
                "img": None,
                "tier": self.core_manager.default_tier,
                "type": self.core_manager.default_type,
                "price": 777,
                "link": "Test Potion link",
                "game_id": f"test_potion_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": False,
                "tox_points": 25,
                "charges": 3,
                "duration_sec": 45,
                "potion_type": "potion",
            }
        else:
            raise ValueError(f"Unsupported model: {model.__name__}")

    def get_models_creation_map(self):
        """
        Get a mapping of models to their corresponding creation methods.

        Returns:
            dict: A dictionary mapping model classes to their respective creation methods.
        """
        return {
            Bomb: self.create_bomb,
            Oil: self.create_oil,
            Potion: self.create_potion,
        }
