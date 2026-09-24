from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0009_migrate_blocks'),
    ]

    operations = [
        migrations.RemoveField(model_name='toolcommand', name='command_category'),
        migrations.RenameField(
            model_name='toolcommand',
            old_name='new_category',
            new_name='command_category',
        ),
    ]
