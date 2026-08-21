from django.db import models
from attacks.models import Attack



class PortCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Port Categories"

    def __str__(self):
        return self.name


class Port(models.Model):
    category = models.ForeignKey(PortCategory, on_delete=models.CASCADE, related_name="ports")
    number = models.PositiveIntegerField()
    service_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=300)
    vulnerability = models.TextField()
    related_attack = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} - {self.service_name}"




