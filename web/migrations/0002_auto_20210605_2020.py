# Generated by Django 3.1.6 on 2021-06-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tugas',
            name='nama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tugas',
            name='judul',
            field=models.CharField(max_length=20),
        ),
    ]
