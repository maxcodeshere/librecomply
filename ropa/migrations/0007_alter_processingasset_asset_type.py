# Generated by Django 5.2.1 on 2025-05-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0006_processingasset_processingactivity_assets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingasset',
            name='asset_type',
            field=models.CharField(max_length=50),
        ),
    ]
