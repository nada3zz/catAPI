from django.http import response
from rest_framework.test import APIClient, APITestCase
from .factories import NonTechCircleFactory, TechCircleFactory
from rest_framework import status

class TechCircleTestCase(APITestCase):
    def setUp(self) -> None:
        self._api_path = "/techcircle/"
        self.circle = TechCircleFactory.create()
        self.client = APIClient()

    def test_retrieve_circle(self):
        response = self.client.get(f"{self._api_path}{self.circle.id}/",content_type="application/json")
        self.assertEqual(response.data['id'],self.circle.id)
        self.assertEqual(response.data['title'], self.circle.title)
        self.assertEqual(response.data['description'], self.circle.description)
    
    def test_retrieve_ar_client(self):
        response = self.client.get(f"{self._api_path}{self.circle.id}/",
                                    content_type="application/json",
                                    **{'HTTP_ACCEPT_LANGUAGE':'ar'})
        self.assertEqual(response.data['id'],self.circle.id)
        self.assertEqual(response.data['title'], self.circle.title_ar)
        self.assertEqual(response.data['description'], self.circle.description_ar)
    
    def test_delete_circle(self):
        response = self.client.delete(f"{self._api_path}{self.circle.id}/",content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_circle(self):
        response = self.client.patch(f"{self._api_path}{self.circle.id}/",content_type="application/json", data={'title':'test'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_list_circles(self):
        response = self.client.get(f"{self._api_path}",
                                    content_type="application/json")
        self.assertEqual(response.data[0]['id'],self.circle.id)
        self.assertEqual(response.data[0]['title'], self.circle.title)
        self.assertEqual(response.data[0]['description'], self.circle.description)
    
    def test_unsupported_language(self):
        response = self.client.get(f"{self._api_path}{self.circle.id}/",
                                    content_type="application/json",
                                    **{'HTTP_ACCEPT_LANGUAGE':'es'})
        self.assertEqual(response.data['id'],self.circle.id)
        self.assertEqual(response.data['title'], self.circle.title)
        self.assertEqual(response.data['description'], self.circle.description)

class NonTechCircleTest(TechCircleTestCase):
    def setUp(self) -> None:
        self._api_path = "/nontechcicle/"
        self.circle = NonTechCircleFactory.create()
        self.client = APIClient()
