from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  # Ensure this exists
    purchase_date = models.DateField(null=True, blank=True)  # Ensure this exists
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')  # Ensure this exists

    def __str__(self):
        return self.name
