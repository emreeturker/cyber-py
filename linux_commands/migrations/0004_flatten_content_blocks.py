from django.db import migrations


def flatten(apps, schema_editor):
    LinuxCommandCategory = apps.get_model("linux_commands", "LinuxCommandCategory")
    LinuxCommandElement = apps.get_model("linux_commands", "LinuxCommandElement")

    for category in LinuxCommandCategory.objects.all():
        order = 0

        # The category's own flat commands (LinuxCommand) come first, in
        # their existing position order, matching how they render today
        # above the category's content blocks.
        for command in category.commands.order_by("position"):
            LinuxCommandElement.objects.create(
                category=category, order=order, element_type="command",
                command_text=command.command,
                description_text=command.description,
            )
            order += 1
            if command.image:
                LinuxCommandElement.objects.create(
                    category=category, order=order, element_type="image",
                    image=command.image,
                )
                order += 1

        blocks = category.content_blocks.order_by("order")
        for block in blocks:
            if block.name:
                LinuxCommandElement.objects.create(
                    category=category, order=order, element_type="title", text=block.name,
                )
                order += 1

            if block.description:
                LinuxCommandElement.objects.create(
                    category=category, order=order, element_type="description",
                    description_text=block.description,
                )
                order += 1

            if block.image:
                LinuxCommandElement.objects.create(
                    category=category, order=order, element_type="image", image=block.image,
                )
                order += 1

            if block.related_attack_id or block.related_tool_id:
                LinuxCommandElement.objects.create(
                    category=category, order=order, element_type="link",
                    text=block.button_label,
                    link_attack_id=block.related_attack_id,
                    link_tool_id=block.related_tool_id,
                )
                order += 1


class Migration(migrations.Migration):

    dependencies = [
        ('linux_commands', '0003_linuxcommandelement'),
    ]

    operations = [
        migrations.RunPython(flatten, migrations.RunPython.noop),
    ]
