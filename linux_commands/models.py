from django.db import models
from common.models import BaseCommand



class LinuxCommandCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Linux Command Categories"  

    def __str__(self):
        return self.name
    

class LinuxCommand(BaseCommand):
    category = models.ForeignKey(LinuxCommandCategory, on_delete=models.CASCADE, related_name="commands")

    def __str__(self):
        return self.command    
