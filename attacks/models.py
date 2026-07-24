from django.db import models
from common.models import TimeStamped


class AttackCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Attack Categories"
        
    def __str__(self):
        return self.name
    

class Attack(TimeStamped):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(AttackCategory, on_delete=models.PROTECT, related_name="attacks")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class AttackCommand(models.Model):
    description = models.TextField()
    command = models.CharField(max_length=200)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="commands")

    def __str__(self):
        return self.command