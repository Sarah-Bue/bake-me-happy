# Generated by Django 4.2.18 on 2025-03-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('general', 'General Inquiry'), ('order', 'Order Information'), ('feedback', 'Feedback'), ('custom', 'Order Customization Request'), ('Catering', 'Catering Inquiry'), ('other', 'Other')], default='', max_length=100),
        ),
    ]
