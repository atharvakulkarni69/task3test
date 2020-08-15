# Generated by Django 3.0.9 on 2020-08-15 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='email',
        ),
        migrations.RemoveField(
            model_name='info',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='info',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='info',
            name='pd',
        ),
        migrations.RemoveField(
            model_name='info',
            name='uname',
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]