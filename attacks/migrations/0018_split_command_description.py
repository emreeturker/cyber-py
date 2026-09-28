from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0017_alter_attackcommandelement_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attackcommandelement',
            old_name='description_text',
            new_name='block_description',
        ),
        migrations.AlterField(
            model_name='attackcommandelement',
            name='block_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='attackcommandelement',
            name='command_description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
    ]
