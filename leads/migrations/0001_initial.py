# Generated by Django 3.1.4 on 2021-07-30 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('special_file', models.FileField(blank=True, null=True, upload_to='')),
                ('phoned', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.salesagent')),
            ],
        ),
    ]
