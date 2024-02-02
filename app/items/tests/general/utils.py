from uuid import uuid4

from core.tests.utils import CoreTestManager
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.urls import reverse

from ...models.general_models import (
    BaseItem,
    CraftingComponent,
    Recipe,
    RecipeComponent,
    Source,
)
from ...serializers.general_serializers import (
    CraftingComponentSerializer,
    RecipeComponentSerializer,
    RecipeSerializer,
    SourceSerializer,
)


class ItemsTestManager:
    """
    A test manager for handling operations related to testing in the Items application.

    This class provides various methods to create instances of models like BaseItem,
    CraftingComponent, Recipe, RecipeComponent, and Source. It also includes utility
    methods for generating URLs for these instances and serializing them.

    Attributes:
        core_manager (CoreTestManager): An instance of CoreTestManager for core functionalities.
        user (User): A user instance created for testing purposes.
        _base_item (BaseItem): A BaseItem instance created for testing.
        _base_recipe (Recipe): A Recipe instance created for testing.
    """

    def __init__(self) -> None:
        self.core_manager = CoreTestManager()
        self.user = self.core_manager.create_user(email="items.test.user@example.com", password="testpass")
        self._base_item = self.create_base_item(self.user)
        self._base_recipe = self.create_recipe(self.user)

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
            CraftingComponent: "items:general:crafting-components-list",
            Recipe: "items:general:recipes-list",
            RecipeComponent: "items:general:recipes-components-list",
            Source: "items:general:sources-list",
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
            CraftingComponent: "items:general:crafting-components-detail",
            Recipe: "items:general:recipes-detail",
            RecipeComponent: "items:general:recipes-components-detail",
            Source: "items:general:sources-detail",
        }
        try:
            return reverse(model_to_url[model], args=[id])
        except KeyError:
            raise ValueError(f"Unknown model: {model}")

    @staticmethod
    def instance_img_upload(model: type, id: int) -> str:
        """
        Generate the URL for image upload for an instance of a specific model by its ID.

        Args:
            model (type): The Django model class for which to generate the image upload URL.
            id (int): The ID of the instance for which to generate the URL.

        Returns:
            str: The URL for retrieving details of the specified model instance.

        Raises:
            ValueError: If the provided model is not recognized.
        """

        model_to_url = {
            CraftingComponent: "items:general:crafting-components-upload-img",
            Recipe: "items:general:recipes-upload-img",
            RecipeComponent: "items:general:recipes-components-upload-img",
            Source: "items:general:sources-upload-img",
        }
        try:
            return reverse(model_to_url[model], args=[id])
        except KeyError:
            raise ValueError(f"Unknown model: {model}")

    def create_base_item(self, user, **params) -> BaseItem:
        """Create a new BaseItem instance."""
        return self._create_instance(user, BaseItem, **params)

    def create_crafting_component(self, user, **params) -> CraftingComponent:
        """Create a new CraftingComponent instance."""
        return self._create_instance(user, CraftingComponent, **params)

    def create_crafting_component_item_with_source(self, user) -> BaseItem:
        """Create a new BaseItem instance with source."""
        craft_comp = self.create_crafting_component(user)
        source = self.create_source(user, item=craft_comp)
        craft_comp.sources.add(source)
        return craft_comp

    def create_recipe(self, user, **params) -> Recipe:
        """Create a new Recipe instance."""
        return self._create_instance(user, Recipe, **params)

    def create_recipe_component(self, **params) -> RecipeComponent:
        """Create a new RecipeComponent instance."""
        return self._create_instance(None, RecipeComponent, **params)

    def create_source(self, user, **params) -> Source:
        """Create a new Source instance."""
        return self._create_instance(user, Source, **params)

    def _create_instance(self, user: get_user_model(), model: Model, **params: dict):
        """
        Private method to create an instance of a given model with specified parameters.

        This method is intended for internal use to ensure consistency in instance creation.

        Args:
            user (User): The user associated with the instance.
            model (Model): The Django model class of the instance to be created.
            **params (dict): A dictionary of parameters for the instance.

        Returns:
            An instance of the specified model.

        Note:
            This method is private and should not be called directly.
        """
        # private in order to avoid unexcpected model for which we don't have a payload
        payload = self.get_default_model_payload(model)
        payload.update(**params)
        if user:
            instance = model.objects.create(user=user, **payload)
        else:
            instance = model.objects.create(**payload)
        return instance

    def serialize_instance(self, instance):
        """
        Serialize a model instance using the appropriate serializer.

        This method uses the model_serializer_map to find the correct serializer for
        the given instance and then returns the serialized data.

        Args:
            instance (Model instance): The instance to be serialized.

        Returns:
            dict: The serialized data of the instance.
        """

        model_serializer_map = {
            CraftingComponent: CraftingComponentSerializer,
            Recipe: RecipeSerializer,
            RecipeComponent: RecipeComponentSerializer,
            Source: SourceSerializer,
        }

        serializer_class = model_serializer_map[type(instance)]
        serializer = serializer_class(instance=instance)
        return serializer.data

    def get_default_model_payload(self, model: Model) -> dict:
        """
        Get the default payload for creating an instance of the given model.

        This method provides a pre-defined set of default values for creating
        instances of different models used in the Items app.

        Args:
            model (Model): The Django model class for which to generate the payload.

        Returns:
            dict: A dictionary containing default values for the model instance.

        Raises:
            ValueError: If the model is not supported or recognized.
        """

        if model == BaseItem:
            return {
                "name": "Test Base item",
                "description": "Test BaseItem description",
                "tier": self.core_manager.default_tier,
                "type": self.core_manager.default_type,
                "price": 777,
                "link": "Test Base item link",
                "game_id": f"base_item_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": False,
            }
        elif model == CraftingComponent:
            return {
                "name": "Test Crafting component",
                "description": "Test CraftingComponent description",
                "tier": self.core_manager.default_tier,
                "type": self.core_manager.default_type,
                "price": 777,
                "link": "Test Crafting component link",
                "game_id": f"crafting_component_{str(uuid4())[:8]}",
                "craftable": True,
                "dismantlable": False,
                "img": None,
                "craft_type": "alchemy",
            }

        elif model == Source:
            return {
                "item": self._base_item,
                "source": f"Test Source_{str(uuid4())[:8]}",
                "link": "",
            }
        elif model == Recipe:
            return {
                "item": self._base_item,
            }
        elif model == RecipeComponent:
            return {
                "recipe": self._base_recipe,
                "item": self._base_item,
                "quantity": 1,
            }
        else:
            raise ValueError(f"Unsupported model: {model.__name__}")

    def get_models_creation_map(self):
        """
        Get a mapping of models to their corresponding creation methods.

        This method provides a dictionary where keys are model classes and values
        are methods used to create instances of these models.

        Returns:
            dict: A dictionary mapping model classes to their creation methods.
        """

        return {
            CraftingComponent: self.create_crafting_component,
            Recipe: self.create_recipe,
            RecipeComponent: self.create_recipe_component,
            Source: self.create_source,
        }
