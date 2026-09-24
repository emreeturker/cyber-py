from django.db import models
from attacks.models import Attack
from tools.models import Tool



class PortCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Port Categories"

    def __str__(self):
        return self.name


class Port(models.Model):
    category = models.ForeignKey(PortCategory, on_delete=models.CASCADE, related_name="ports")
    number = models.CharField(max_length=20)
    service_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=300)
    vulnerability = models.TextField()
    related_attack = models.ForeignKey(Attack, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    related_tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} - {self.service_name}"


class PortContentBlock(models.Model):
    category = models.ForeignKey(PortCategory, on_delete=models.CASCADE, related_name="content_blocks")
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="port_block_images/%Y/%m/", blank=True, null=True)
    related_attack = models.ForeignKey("attacks.Attack", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_port_blocks")
    related_tool = models.ForeignKey("tools.Tool", on_delete=models.SET_NULL, null=True, blank=True, related_name="linked_from_port_blocks")
    button_label = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __str__(self):
        return f"{self.category.name} - {self.name or 'Untitled block'}"
