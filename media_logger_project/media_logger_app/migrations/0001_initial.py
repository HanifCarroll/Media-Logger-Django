# Generated by Django 2.1.1 on 2018-09-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200, null=True)),
                ('user', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
                ('thumbnail_url', models.CharField(default=None, max_length=200, null=True)),
                ('time_posted', models.DateTimeField(auto_now_add=True, verbose_name='posted at')),
                ('service', models.CharField(max_length=15)),
            ],
        ),
    ]
