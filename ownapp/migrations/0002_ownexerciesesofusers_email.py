# Generated by Django 4.1.3 on 2022-12-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownexerciesesofusers',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
