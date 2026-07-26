from django.db import models
from common.models import TimeStamped, CommandCategory
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
    

class AttackCommand(models.Model):
    description = models.TextField()
    command = models.CharField(max_length=200)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="commands")
    command_category = models.ForeignKey(CommandCategory, on_delete=models.PROTECT, null=True, blank=True, related_name="attack_commands")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.command