# Generated by Django 4.1.2 on 2022-10-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_commande'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='Address',
            new_name='address',
        ),
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=200),
            preserve_default=False,
        ),
    ]
