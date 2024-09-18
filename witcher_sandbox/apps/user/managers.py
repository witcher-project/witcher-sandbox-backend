from typing import Any, Optional

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Custom User Manager"""

    def create_user(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> AbstractUser:
        """Create and return a new user"""
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields: Any) -> AbstractUser:
        """Create and return a new superuser"""
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self.create_user(email, password, **extra_fields)
