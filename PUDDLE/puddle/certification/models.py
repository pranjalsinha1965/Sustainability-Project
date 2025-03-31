from django.db import models

class SustainabilityFactor(models.Model):
    building = models.CharField(max_length=255)  # This can be a ForeignKey if related to a building model
    energy = models.FloatField()
    water = models.FloatField()
    waste_management = models.FloatField()
    building_envelope = models.FloatField()
    other_factors = models.FloatField()

    @property
    def total_score(self):
        return (self.energy * 0.25) + (self.water * 0.13) + (self.waste_management * 0.25) + \
               (self.building_envelope * 0.25) + (self.other_factors * 0.12)

    def __str__(self):
        return f"Sustainability Score for {self.building}"
