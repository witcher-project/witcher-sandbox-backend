# """
# Tests for the user API.
# """
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
#
# CREATE_USER_URL = reverse("user:create")
# TOKEN_URL = reverse("user:token_obtain_pair")
# ME_URL = reverse("user:me")
#
#
# def create_user(**params):
#     """Create and return a new user"""
#     return get_user_model().objects.create_user(**params)
#
#
# class PublicUserAPITests(TestCase):
#     """Test the public features of the user API"""
#
#     def setUp(self):
#         self.client = APIClient()
#         self.payload = {
#             "email": "test@example.com",
#             "password": "testpass",
#             "name": "Test name",
#         }
#
#     def test_create_user_success(self):
#         """Test creating a user is successful"""
#         res = self.client.post(CREATE_USER_URL, self.payload)
#
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         user = get_user_model().objects.get(email=self.payload["email"])
#         self.assertTrue(user.check_password(self.payload["password"]))
#         self.assertNotIn("password", res.data)
#
#     def test_user_with_email_exists_error(self):
#         """Test returned error if user with provided email exists"""
#         create_user(**self.payload)
#         res = self.client.post(CREATE_USER_URL, self.payload)
#
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_password_too_short_error(self):
#         """Test returned error if password less than 5 characters"""
#         self.payload["password"] = "ab"
#
#         res = self.client.post(CREATE_USER_URL, self.payload)
#
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#         user_exists = get_user_model().objects.filter(email=self.payload["email"]).exists()
#         self.assertFalse(user_exists)
#
#     def test_create_token_for_user(self):
#         """Testing token generation for valid credentials"""
#         payload = self.payload
#         payload["password"] = "test_user_password"
#
#         create_user(**payload)
#
#         token_payload = {"email": payload["email"], "password": payload["password"]}
#
#         res = self.client.post(TOKEN_URL, token_payload)
#
#         self.assertIn("refresh", res.data)
#         self.assertIn("access", res.data)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#
#     def test_create_token_bad_credentials(self):
#         """Test returns error if credentials are invalid"""
#         create_user(**self.payload)
#
#         payload = self.payload
#         payload["email"] = ""
#         payload["password"] = "badpass"
#
#         res = self.client.post(TOKEN_URL, payload)
#
#         self.assertNotIn("token", res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_create_token_blank_password(self):
#         """Test posting a blank password returns an error"""
#         payload = self.payload
#         payload["email"] = "test@example.com"
#         payload["password"] = ""
#
#         res = self.client.post(TOKEN_URL, payload)
#
#         self.assertNotIn("refresh", res.data)
#         self.assertNotIn("access", res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_retrieve_user_unauthorized(self):
#         """Test authentication is required for user"""
#         res = self.client.get(ME_URL)
#
#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
#
#
# class PrivateUserAPITests(TestCase):
#     """Test API requests that require authentication"""
#
#     def setUp(self):
#         self.payload = {
#             "email": "test@example.com",
#             "password": "testpass",
#             "name": "Test name",
#         }
#         self.user = create_user(**self.payload)
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#
#     def test_retrieve_profile_success(self):
#         """Test retrieving profile for logged in user"""
#         res = self.client.get(ME_URL)
#
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(res.data, {"name": self.user.name, "email": self.user.email})
#
#     def test_post_me_not_allowed(self):
#         """Test POST in not allowed for the me endpoint"""
#         res = self.client.post(ME_URL, {})
#
#         self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     def test_update_user_profile(self):
#         """Test updating the user profile for the authenticated user"""
#         payload = self.payload
#         payload["name"] = "Changed name"
#         payload["password"] = "changed_password"
#
#         res = self.client.patch(ME_URL, payload)
#
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.name, payload["name"])
#         self.assertTrue(self.user.check_password(payload["password"]))
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
