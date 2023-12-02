from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo

class TodoIntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(
            title="Test Todo",
            details="Test details",
            status="OPEN"
        )

    def test_index_view(self):
        response = self.client.get(reverse('todo'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")



#tests