from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0014_alter_toolcommandelement_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toolcommandelement',
            old_name='description_text',
            new_name='block_description',
        ),
        migrations.AlterField(
            model_name='toolcommandelement',
            name='block_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='toolcommandelement',
            name='command_description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
    ]
