# Generated by Django 4.0.5 on 2022-07-05 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordpress', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Poll',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='blog',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='title',
            new_name='question',
        ),
    ]
