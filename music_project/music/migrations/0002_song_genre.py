# Generated by Django 3.1.7 on 2021-04-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
