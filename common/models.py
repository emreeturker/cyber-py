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


class BaseCommand(models.Model):
    description = models.TextField()
    command = models.CharField(max_length=200)
    command_category = models.ForeignKey(CommandCategory, on_delete=models.PROTECT, null=True, blank=True, related_name="%(class)s_set+")
    position = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="command_screenshots/%Y/%m/", blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["position"]
            

