# Generated by Django 3.1.4 on 2020-12-14 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20201214_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='participant',
        ),
        migrations.AddField(
            model_name='notification',
            name='mturk_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
