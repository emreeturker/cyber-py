from django.db import migrations
from django.db.models import Min


def copy_categories(apps, schema_editor):
    AttackCommand = apps.get_model("attacks", "AttackCommand")
    AttackCommandCategory = apps.get_model("attacks", "AttackCommandCategory")

    for command in AttackCommand.objects.exclude(command_category=None):
        first_position = AttackCommand.objects.filter(
            attack_id=command.attack_id,
            command_category_id=command.command_category_id,
        ).aggregate(m=Min("position"))["m"] or 0

        category, _ = AttackCommandCategory.objects.get_or_create(
            attack_id=command.attack_id,
            name=command.command_category.name,
            defaults={"order": first_position},
        )
        command.new_category = category
        command.save(update_fields=["new_category"])


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0008_attackcommandcategory_attackcommand_new_category'),
    ]

    operations = [
        migrations.RunPython(copy_categories, migrations.RunPython.noop),
    ]
