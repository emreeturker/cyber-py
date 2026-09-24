from django.db import models
from common.models import TimeStamped, BaseCommand
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
    

class ToolContentBlock(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="content_blocks")
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="tool_block_images/%Y/%m/", blank=True, null=True)
    related_attack = models.ForeignKey("attacks.Attack", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_tool_blocks")
    related_tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_tool_blocks")
    button_label = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __str__(self):
        return f"{self.tool.name} - {self.name or 'Untitled block'}"


class ToolCommand(BaseCommand):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="commands")
    command_category = models.ForeignKey(ToolContentBlock, on_delete=models.PROTECT, null=True, blank=True, related_name="commands")
    
    def __str__(self):
        return self.command
    
