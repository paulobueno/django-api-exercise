from django.db import models


class Property(models.Model):
    friendly_id = models.CharField(max_length=100, unique=True)
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
        ordering = ['-creation_timestamp']
