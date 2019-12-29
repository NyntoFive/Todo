# Generated by Django 2.2.8 on 2019-12-29 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 9, 31, 38, 639152)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('D', 'danger'), ('D', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
