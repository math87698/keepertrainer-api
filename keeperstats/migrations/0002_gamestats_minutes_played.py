# Generated by Django 3.0.3 on 2020-03-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeperstats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestats',
            name='minutes_played',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
