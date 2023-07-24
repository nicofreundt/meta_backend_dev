from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
    def setUp(self):
        models.Menu.objects.create(
            title="Hot Dog",
            price=3.50,
            inventory=250
        )

    def test_create_item(self):
        item = models.Menu.objects.create(
            title="IceCream",
            price=1.5,
            inventory=150
        )
        self.assertEqual(models.Menu.objects.count(), 2)
        self.assertEqual(str(item), "IceCream : 1.5")
