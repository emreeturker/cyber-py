from django.db import migrations

# (tool_slug, name, description, related_attack_slug, button_label)
EXTRA_BLOCKS = [
    ("bettercap", "Example Usage",
     "Below is a real-world demonstration of Bettercap performing an automated MITM attack — see the full attack walkthrough here.",
     "mitm-automatic", "View MITM Automatic Attack"),
    ("metasploit", "Example Usage",
     "Below is a real-world exploitation example using Metasploit — see the full attack walkthrough here.",
     "ftp-exploitation", "View FTP Exploitation"),
    ("metasploit", "", "", "samba-exploitation", "View Samba Exploitation"),
    ("metasploit", "", "", "postgresql-exploitation", "View PostgreSQL Exploitation"),
    ("metasploit", "", "", "ssh-brute-force", "View SSH Brute-Force"),
    ("metasploit", "", "", "vnc-brute-force", "View VNC Brute-Force"),
]


def migrate(apps, schema_editor):
    Tool = apps.get_model("tools", "Tool")
    ToolCommand = apps.get_model("tools", "ToolCommand")
    Block = apps.get_model("tools", "ToolContentBlock")
    Attack = apps.get_model("attacks", "Attack")

    for tool in Tool.objects.all():
        next_order = 1
        for command in ToolCommand.objects.filter(tool=tool).exclude(command_category=None).order_by("position", "id"):
            block, created = Block.objects.get_or_create(
                tool=tool, name=command.command_category.name, defaults={"order": next_order},
            )
            if created:
                next_order += 1
            command.new_category = block
            command.save(update_fields=["new_category"])

        for slug, name, desc, attack_slug, label in EXTRA_BLOCKS:
            if slug != tool.slug:
                continue
            last = Block.objects.filter(tool=tool).order_by("-order").first()
            Block.objects.create(
                tool=tool, name=name, description=desc, button_label=label,
                related_attack=Attack.objects.filter(slug=attack_slug).first(),
                order=(last.order if last else 0) + 1,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0008_content_block'),
        ('attacks', '0013_content_block_sortable'),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop),
    ]
