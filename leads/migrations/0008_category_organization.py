# Generated by Django 3.1.4 on 2021-08-02 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20210802_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
