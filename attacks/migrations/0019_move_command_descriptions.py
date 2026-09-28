from django.db import migrations


def move_command_descriptions(apps, schema_editor):
    AttackCommandElement = apps.get_model("attacks", "AttackCommandElement")
    for element in AttackCommandElement.objects.filter(element_type="command").exclude(block_description=""):
        element.command_description = element.block_description
        element.block_description = ""
        element.save(update_fields=["command_description", "block_description"])


def move_back(apps, schema_editor):
    AttackCommandElement = apps.get_model("attacks", "AttackCommandElement")
    for element in AttackCommandElement.objects.filter(element_type="command").exclude(command_description=""):
        element.block_description = element.command_description
        element.command_description = ""
        element.save(update_fields=["command_description", "block_description"])


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0018_split_command_description'),
    ]

    operations = [
        migrations.RunPython(move_command_descriptions, move_back),
    ]
