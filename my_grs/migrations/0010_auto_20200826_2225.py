# Generated by Django 3.1 on 2020-08-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grs', '0009_auto_20200826_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.TextField(blank=True, default='None', max_length=2000),
        ),
    ]