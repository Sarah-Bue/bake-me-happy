# Generated by Django 4.2.18 on 2025-03-03 14:04

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('bio', django_summernote.fields.SummernoteTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='bakers/')),
                ('order', models.PositiveIntegerField(default=0, help_text='Order in which baker appears on the page')),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
    ]
