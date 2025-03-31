from django.db import models

class SustainabilityFactor(models.Model):
    name = models.CharField(max_length=100)
    weightage = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def weighted_score(self):
        return self.score * (self.weightage / 100) if self.score else 0

class Cooperative(models.Model):
    name = models.CharField(max_length=100)
    number_of_banks = models.PositiveIntegerField()
    number_of_branches = models.PositiveIntegerField()

class Bank(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('Government', 'Government'), 
        ('Private', 'Private'), 
        ('International', 'International')
    ])
    number_of_branches = models.PositiveIntegerField()

class ITI(models.Model):
    name = models.CharField(max_length=100)
    target_segments = models.TextField()

class DISCOM(models.Model):
    name = models.CharField(max_length=100)
    service_area = models.TextField()


