# Generated by Django 5.0.1 on 2024-01-14 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0008_auto_20210519_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='give_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 16, 37, 2, 776804)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='take_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 16, 37, 2, 776804)),
        ),
    ]
