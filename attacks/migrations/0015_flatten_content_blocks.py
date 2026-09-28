from django.db import migrations


def flatten(apps, schema_editor):
    Attack = apps.get_model("attacks", "Attack")
    AttackCommandElement = apps.get_model("attacks", "AttackCommandElement")

    for attack in Attack.objects.all():
        order = 0
        blocks = attack.command_categories.order_by("order").prefetch_related("commands")
        for block in blocks:
            if block.name:
                AttackCommandElement.objects.create(
                    attack=attack, order=order, element_type="title", text=block.name,
                )
                order += 1

            if block.description:
                AttackCommandElement.objects.create(
                    attack=attack, order=order, element_type="description",
                    description_text=block.description,
                )
                order += 1

            for command in block.commands.order_by("position"):
                AttackCommandElement.objects.create(
                    attack=attack, order=order, element_type="command",
                    command_text=command.command,
                    description_text=command.description,
                )
                order += 1
                if command.image:
                    AttackCommandElement.objects.create(
                        attack=attack, order=order, element_type="image",
                        image=command.image,
                    )
                    order += 1

            if block.image:
                AttackCommandElement.objects.create(
                    attack=attack, order=order, element_type="image", image=block.image,
                )
                order += 1

            if block.related_attack_id or block.related_tool_id:
                AttackCommandElement.objects.create(
                    attack=attack, order=order, element_type="link",
                    text=block.button_label,
                    link_attack_id=block.related_attack_id,
                    link_tool_id=block.related_tool_id,
                )
                order += 1


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0014_attackcommandelement'),
    ]

    operations = [
        migrations.RunPython(flatten, migrations.RunPython.noop),
    ]
