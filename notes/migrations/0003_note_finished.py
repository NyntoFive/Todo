# Generated by Django 2.2.8 on 2019-12-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20191229_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
