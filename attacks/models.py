from django.db import models
from common.models import TimeStamped, BaseCommandElement
from django.urls import reverse


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
    
    @property
    def type_label(self):
        return "attack"
    
    @property
    def badge_color(self):
        return "danger"

    def get_absolute_url(self):
        return reverse('attacks:detail', args=[self.slug])
    

class AttackCommandElement(BaseCommandElement):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="elements")