# Generated by Django 3.1.4 on 2021-08-02 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20210802_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='organization',
        ),
    ]