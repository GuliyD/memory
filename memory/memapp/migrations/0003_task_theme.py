# Generated by Django 3.1.1 on 2020-09-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='theme',
            field=models.CharField(default='none theme', max_length=120),
        ),
    ]
