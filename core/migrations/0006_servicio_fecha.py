# Generated by Django 2.2.7 on 2020-10-15 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200930_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
