# Generated by Django 3.1 on 2020-08-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grs', '0003_auto_20200806_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
