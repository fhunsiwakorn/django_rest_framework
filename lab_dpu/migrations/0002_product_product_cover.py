# Generated by Django 5.0.4 on 2024-04-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_dpu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_cover',
            field=models.CharField(blank=True, default=None, max_length=128),
        ),
    ]
