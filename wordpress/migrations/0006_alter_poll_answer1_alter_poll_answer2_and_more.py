# Generated by Django 4.0.6 on 2022-07-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordpress', '0005_poll_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='answer1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poll',
            name='answer2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='answer3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='answer4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(max_length=50),
        ),
    ]
