from django.db import models

class Certification(models.Model):
    certificate_name = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.certificate_name
