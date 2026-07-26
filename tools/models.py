from django.db import models
from common.models import TimeStamped, CommandCategory
from django.urls import reverse



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
    
    @property
    def type_label(self):
        return "tool"
    
    @property
    def badge_color(self):
        return "primary"

    def get_absolute_url(self):
        return reverse('tools:detail', args=[self.slug])
    

class ToolCommand(models.Model):
    description = models.TextField()
    command = models.CharField(max_length=200)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="commands")
    command_category = models.ForeignKey(CommandCategory, on_delete=models.PROTECT, null=True, blank=True, related_name="tool_commands")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.command
    
