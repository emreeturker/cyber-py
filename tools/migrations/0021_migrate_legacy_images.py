from django.db import migrations


def migrate_forward(apps, schema_editor):
    ToolCommandElement = apps.get_model("tools", "ToolCommandElement")
    ToolCommandElementImage = apps.get_model("tools", "ToolCommandElementImage")

    for element in ToolCommandElement.objects.exclude(image=""):
        ToolCommandElementImage.objects.create(
            element=element, order=0, image=element.image.name,
        )
        element.image = ""
        element.save(update_fields=["image"])


def migrate_backward(apps, schema_editor):
    ToolCommandElement = apps.get_model("tools", "ToolCommandElement")
    ToolCommandElementImage = apps.get_model("tools", "ToolCommandElementImage")

    for image in ToolCommandElementImage.objects.filter(order=0):
        element = image.element
        if not element.image:
            element.image = image.image.name
            element.save(update_fields=["image"])
            image.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0020_toolcommandelementimage'),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
