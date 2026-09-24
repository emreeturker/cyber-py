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


class LinuxCommandContentBlock(models.Model):
    category = models.ForeignKey(LinuxCommandCategory, on_delete=models.CASCADE, related_name="content_blocks")
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="linux_block_images/%Y/%m/", blank=True, null=True)
    related_attack = models.ForeignKey("attacks.Attack", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_linux_blocks")
    related_tool = models.ForeignKey("tools.Tool", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_linux_blocks")
    button_label = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __str__(self):
        return f"{self.category.name} - {self.name or 'Untitled block'}"
