from django.db import migrations

METASPLOIT_TEXT = "This attack was carried out using Metasploit Framework — see the full command reference here."

# (attack_slug, position, name, description, related_attack_slug, related_tool_slug, button_label)
BLOCKS = [
    ("ssh-brute-force", "before", "First Step",
     "Before running this attack, verified usernames should be gathered instead of guessing blindly — see how to enumerate valid SMTP accounts here.",
     "smtp-user-enumeration-port-25", None, "View SMTP User Enumeration Details"),
    ("mitm-automatic", "after", "Tool Used",
     "This attack was carried out using Bettercap — see the full command reference here.",
     None, "bettercap", "View Bettercap Details"),
    ("mitm-manual", "after", "Automated Version Available",
     "This same attack can also be performed faster and more efficiently using Bettercap's automated workflow.",
     "mitm-automatic", None, "View MITM Automatic"),
    ("ftp-exploitation", "after", "Tool Used", METASPLOIT_TEXT, None, "metasploit", "View Metasploit Details"),
    ("samba-exploitation", "after", "Tool Used", METASPLOIT_TEXT, None, "metasploit", "View Metasploit Details"),
    ("postgresql-exploitation", "after", "Tool Used", METASPLOIT_TEXT, None, "metasploit", "View Metasploit Details"),
    ("ssh-brute-force", "after", "Tool Used", METASPLOIT_TEXT, None, "metasploit", "View Metasploit Details"),
    ("vnc-brute-force", "after", "Tool Used", METASPLOIT_TEXT, None, "metasploit", "View Metasploit Details"),
    ("smtp-user-enumeration-port-25", "after", "Next Step",
     "The usernames discovered above can be fed into an SSH Brute-Force attack using Metasploit's ssh_login module — see the full command reference and discovered credentials here.",
     "ssh-brute-force", None, "View SSH Brute-Force Details"),
    ("fallback-unknown-ports", "after", "Real-World Example",
     "See this methodology applied step by step against a real unlisted service — an outdated distcc daemon exploited via CVE-2004-2687.",
     "distcc-port-3632", None, "View distcc (Port 3632)"),
    ("distcc-port-3632", "after", "Methodology Reference",
     "This attack follows the general fallback methodology for unknown/unlisted ports — see the full step-by-step approach here.",
     "fallback-unknown-ports", None, "View Unknown/Unlisted Ports"),
]


def seed(apps, schema_editor):
    Attack = apps.get_model("attacks", "Attack")
    Category = apps.get_model("attacks", "AttackCommandCategory")
    Tool = apps.get_model("tools", "Tool")

    for attack in Attack.objects.filter(command_categories__isnull=False).distinct():
        for i, cat in enumerate(Category.objects.filter(attack=attack).order_by("order", "id"), start=1):
            cat.order = i
            cat.save(update_fields=["order"])

    for slug, where, name, desc, rel_attack, rel_tool, label in BLOCKS:
        attack = Attack.objects.filter(slug=slug).first()
        if attack is None:
            continue
        if where == "before":
            order = 0
        else:
            last = Category.objects.filter(attack=attack).order_by("-order").first()
            order = (last.order if last else 0) + 1
        Category.objects.update_or_create(
            attack=attack,
            name=name,
            defaults={
                "description": desc,
                "related_attack": Attack.objects.filter(slug=rel_attack).first() if rel_attack else None,
                "related_tool": Tool.objects.filter(slug=rel_tool).first() if rel_tool else None,
                "button_label": label,
                "order": order,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0011_category_related_tool'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
