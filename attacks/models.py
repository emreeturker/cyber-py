from django.db import models
from common.models import TimeStamped, BaseCommand
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
    

class AttackCommandCategory(models.Model):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="command_categories")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  
    image = models.ImageField(upload_to="category_images/%Y/%m/", blank=True, null=True)
    related_attack = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_categories")
    related_tool = models.ForeignKey("tools.Tool", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_attack_categories")
    button_label = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["attack", "order"]
        unique_together = ("attack", "name")
        verbose_name_plural = "Attack Command Categories"

    def __str__(self):
        return f"{self.attack.name} - {self.name}"


class AttackCommand(BaseCommand):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, related_name="commands")
    command_category = models.ForeignKey(AttackCommandCategory, on_delete=models.PROTECT, null=True, blank=True, related_name="commands")
    
    def __str__(self):
        return self.command