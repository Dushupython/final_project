# Generated by Django 3.0.4 on 2020-04-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20200419_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='telegram_id'),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='trigger_price',
            field=models.IntegerField(verbose_name='Price Alert'),
        ),
    ]
