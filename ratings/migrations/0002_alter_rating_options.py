# Generated by Django 4.0.7 on 2024-02-05 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-timestamp']},
        ),
    ]
