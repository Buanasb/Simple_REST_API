# Generated by Django 3.1.6 on 2021-06-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210605_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='judul_PI',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
