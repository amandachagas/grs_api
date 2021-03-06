# Generated by Django 3.1 on 2020-08-06 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie_id', models.PositiveIntegerField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=150)),
                ('year', models.PositiveIntegerField()),
                ('imdb_id', models.CharField(blank=True, default='None', max_length=50)),
                ('imdb_link', models.CharField(blank=True, default='None', max_length=200)),
                ('poster', models.CharField(blank=True, default='None', max_length=500)),
                ('youtubeId', models.CharField(blank=True, default='None', max_length=50)),
                ('tags', models.CharField(blank=True, default='None', max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_grs.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
    ]
