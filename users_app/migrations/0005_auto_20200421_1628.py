# Generated by Django 3.0.4 on 2020-04-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_auto_20200421_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
