from unittest import TestCase
from rest_framework.test import APIClient


class TestSmth(TestCase):
    def test_sample_view_ok(self):
        client = APIClient()
        url = '/api/v1/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
