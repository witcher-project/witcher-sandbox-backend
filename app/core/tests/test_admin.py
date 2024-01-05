"""
Tests for django admin modifications
"""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass"
        )
        self.admin_user = get_user_model().objects.create_superuser(
            email="superuser@example.com",
            password="testpass"
        )
        self.client.force_login(self.admin_user)

    def test_user_list(self):
        """Test that users are listed on page."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Tests that edit user page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
