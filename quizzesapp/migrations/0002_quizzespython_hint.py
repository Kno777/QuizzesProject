# Generated by Django 4.1.3 on 2022-12-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzespython',
            name='hint',
            field=models.TextField(blank=True),
        ),
    ]
