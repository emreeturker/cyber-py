from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0009_migrate_categories'),
    ]

    operations = [
        migrations.RemoveField(model_name='attackcommand', name='command_category'),
        migrations.RenameField(
            model_name='attackcommand',
            old_name='new_category',
            new_name='command_category',
        ),
    ]
