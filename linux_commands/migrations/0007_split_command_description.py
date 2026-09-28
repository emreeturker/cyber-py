from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linux_commands', '0006_alter_linuxcommandelement_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linuxcommandelement',
            old_name='description_text',
            new_name='block_description',
        ),
        migrations.AlterField(
            model_name='linuxcommandelement',
            name='block_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='linuxcommandelement',
            name='command_description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
    ]
