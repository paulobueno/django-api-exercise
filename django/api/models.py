from django.db import models
import random
import string


class Property(models.Model):
    friendly_id = models.CharField(max_length=100, unique=True, db_index=True)
    guests_max_number = models.PositiveIntegerField()
    bathrooms_quantity = models.PositiveIntegerField()
    accepts_animals = models.BooleanField(default=False)
    cleaning_cost = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.friendly_id

    class Meta:
        ordering = ['-update_timestamp']
        verbose_name_plural = 'Properties'


class Listing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='listings')
    published_platform = models.CharField(max_length=100)
    published_platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Listing for {self.property.friendly_id} on {self.published_platform}"

    class Meta:
        ordering = ['-update_timestamp']


def generate_booking_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=4) + random.choices(string.digits, k=4))
        if not Booking.objects.filter(booking_code=code).exists():
            return code

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    booking_code = models.CharField(max_length=8, unique=True, default=generate_booking_code, db_index=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField()
    guests_quantity = models.PositiveIntegerField()
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.booking_code} for {self.listing.property.friendly_id}"

    class Meta:
        ordering = ['-update_timestamp']
