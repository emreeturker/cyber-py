from django.db import models
from core.models import TimeStamped


class ToolCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tool Categories"

    def __str__(self):
        return self.name
    

class Tool(TimeStamped):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ToolCategory, on_delete=models.PROTECT, related_name="tools")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class ToolCommand(models.Model):
    description = models.TextField()
    command = models.CharField(max_length=200)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="commands")

    def __str__(self):
        return self.command
    
