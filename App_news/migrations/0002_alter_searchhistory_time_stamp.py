# Generated by Django 4.2.5 on 2023-09-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhistory',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
