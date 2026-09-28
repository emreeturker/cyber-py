from django.db import migrations


def flatten(apps, schema_editor):
    Tool = apps.get_model("tools", "Tool")
    ToolCommandElement = apps.get_model("tools", "ToolCommandElement")

    for tool in Tool.objects.all():
        order = 0
        blocks = tool.content_blocks.order_by("order").prefetch_related("commands")
        for block in blocks:
            if block.name:
                ToolCommandElement.objects.create(
                    tool=tool, order=order, element_type="title", text=block.name,
                )
                order += 1

            if block.description:
                ToolCommandElement.objects.create(
                    tool=tool, order=order, element_type="description",
                    description_text=block.description,
                )
                order += 1

            for command in block.commands.order_by("position"):
                ToolCommandElement.objects.create(
                    tool=tool, order=order, element_type="command",
                    command_text=command.command,
                    description_text=command.description,
                )
                order += 1
                if command.image:
                    ToolCommandElement.objects.create(
                        tool=tool, order=order, element_type="image",
                        image=command.image,
                    )
                    order += 1

            if block.image:
                ToolCommandElement.objects.create(
                    tool=tool, order=order, element_type="image", image=block.image,
                )
                order += 1

            if block.related_attack_id or block.related_tool_id:
                ToolCommandElement.objects.create(
                    tool=tool, order=order, element_type="link",
                    text=block.button_label,
                    link_attack_id=block.related_attack_id,
                    link_tool_id=block.related_tool_id,
                )
                order += 1


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0011_toolcommandelement'),
    ]

    operations = [
        migrations.RunPython(flatten, migrations.RunPython.noop),
    ]
