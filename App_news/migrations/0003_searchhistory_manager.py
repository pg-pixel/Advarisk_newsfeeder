# Generated by Django 4.2.5 on 2023-09-19 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_news', '0002_alter_searchhistory_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='Manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]