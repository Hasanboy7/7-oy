# Generated by Django 5.0.4 on 2024-04-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crudmodel',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crudmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]