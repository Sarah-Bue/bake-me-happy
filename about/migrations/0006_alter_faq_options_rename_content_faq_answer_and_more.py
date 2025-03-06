# Generated by Django 4.2.18 on 2025-03-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_faq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['order'], 'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQ'},
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='content',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='title',
        ),
        migrations.AddField(
            model_name='faq',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Order in which FAQ appears on the page'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question',
            field=models.CharField(default='Your question here', max_length=500),
        ),
    ]
