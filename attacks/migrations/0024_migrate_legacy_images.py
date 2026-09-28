from django.db import migrations


def migrate_forward(apps, schema_editor):
    AttackCommandElement = apps.get_model("attacks", "AttackCommandElement")
    AttackCommandElementImage = apps.get_model("attacks", "AttackCommandElementImage")

    for element in AttackCommandElement.objects.exclude(image=""):
        AttackCommandElementImage.objects.create(
            element=element, order=0, image=element.image.name,
        )
        element.image = ""
        element.save(update_fields=["image"])


def migrate_backward(apps, schema_editor):
    AttackCommandElement = apps.get_model("attacks", "AttackCommandElement")
    AttackCommandElementImage = apps.get_model("attacks", "AttackCommandElementImage")

    for image in AttackCommandElementImage.objects.filter(order=0):
        element = image.element
        if not element.image:
            element.image = image.image.name
            element.save(update_fields=["image"])
            image.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0023_attackcommandelementimage'),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
