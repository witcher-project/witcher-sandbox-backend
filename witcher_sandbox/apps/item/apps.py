from django.apps import AppConfig


class ItemsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "witcher_sandbox.apps.item"

    def ready(self) -> None:
        from .admins import alchemy, general  # noqa
