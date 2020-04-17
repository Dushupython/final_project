# Generated by Django 3.0.4 on 2020-04-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_bitcoin_pair'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bitcoin',
            new_name='Trigger',
        ),
        migrations.AlterField(
            model_name='symbol',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
