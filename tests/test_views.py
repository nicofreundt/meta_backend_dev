from django.test import TestCase, Client
from django.urls import reverse
from restaurant import models, serializers

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        models.Menu.objects.create(
            title="Hot Dog",
            price=3.5,
            inventory=13
        )
        models.Menu.objects.create(
            title="Pizza",
            price=5,
            inventory=15
        )
        models.Menu.objects.create(
            title="Burger",
            price=4,
            inventory=37
        )

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu_items = models.Menu.objects.all()
        serialized_items = serializers.MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serialized_items.data)