from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CommandCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Command Categories"

    def __str__(self):
        return self.name


class BaseCommandElement(models.Model):
    TITLE = "title"
    DESCRIPTION = "description"
    COMMAND = "command"
    IMAGE = "image"
    TYPE_CHOICES = [
        (TITLE, "Title"),
        (DESCRIPTION, "Description"),
        (COMMAND, "Command"),
        (IMAGE, "Image"),
    ]

    order = models.PositiveIntegerField(default=0, db_index=True)
    element_type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)

    text = models.CharField("Name", max_length=200, blank=True)
    block_description = models.TextField("Description", blank=True)
    command_text = models.CharField(max_length=500, blank=True)
    command_description = models.TextField("Description", blank=True)
    command_category = models.ForeignKey(
        CommandCategory, on_delete=models.PROTECT, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_set",
    )
    image = models.ImageField(upload_to="command_element_images/%Y/%m/", blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["order"]

    def _determine_element_type(self):
        if self.command_text:
            return self.COMMAND
        if self.image:
            return self.IMAGE
        if self.block_description:
            return self.DESCRIPTION
        if self.text:
            return self.TITLE
        return ""

    def save(self, *args, **kwargs):
        self.element_type = self._determine_element_type()
        super().save(*args, **kwargs)

    def __str__(self):
        label = self.text or self.command_text or self.block_description
        type_label = self.get_element_type_display() or "Empty"
        return f"{type_label}: {label[:40]}" if label else type_label


class BaseCommandElementImage(models.Model):
    image = models.ImageField(upload_to="command_element_images/%Y/%m/")
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        abstract = True
        ordering = ["order"]

    def __str__(self):
        return f"Image #{self.order}"