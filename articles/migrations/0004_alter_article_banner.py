# Generated by Django 4.2.3 on 2024-05-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]