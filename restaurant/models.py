from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'