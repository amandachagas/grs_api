# Generated by Django 3.1 on 2020-08-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grs', '0006_auto_20200822_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='counter',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]