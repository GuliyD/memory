# Generated by Django 3.1.1 on 2020-09-16 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memapp', '0004_contact_contactphonenumber_contactphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='level',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='tree_id',
        ),
    ]
