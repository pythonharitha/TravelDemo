# Generated by Django 4.1 on 2022-10-10 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc1',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img1',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name1',
            new_name='name',
        ),
    ]
