# Generated by Django 3.0.4 on 2020-04-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='telegram_ID'),
        ),
    ]
