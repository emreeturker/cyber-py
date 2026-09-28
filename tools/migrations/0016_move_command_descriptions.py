from django.db import migrations


def move_command_descriptions(apps, schema_editor):
    ToolCommandElement = apps.get_model("tools", "ToolCommandElement")
    for element in ToolCommandElement.objects.filter(element_type="command").exclude(block_description=""):
        element.command_description = element.block_description
        element.block_description = ""
        element.save(update_fields=["command_description", "block_description"])


def move_back(apps, schema_editor):
    ToolCommandElement = apps.get_model("tools", "ToolCommandElement")
    for element in ToolCommandElement.objects.filter(element_type="command").exclude(command_description=""):
        element.block_description = element.command_description
        element.command_description = ""
        element.save(update_fields=["command_description", "block_description"])


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0015_split_command_description'),
    ]

    operations = [
        migrations.RunPython(move_command_descriptions, move_back),
    ]
