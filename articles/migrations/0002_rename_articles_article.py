# Generated by Django 4.2.3 on 2024-05-24 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='articles',
            new_name='article',
        ),
    ]