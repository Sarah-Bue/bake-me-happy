# Generated by Django 4.2.18 on 2025-02-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
