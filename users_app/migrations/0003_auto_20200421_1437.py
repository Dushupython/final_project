# Generated by Django 3.0.4 on 2020-04-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20200421_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='telegram_id'),
        ),
    ]
