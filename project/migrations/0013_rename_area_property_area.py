# Generated by Django 4.1.2 on 2022-12-01 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_agent_skype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='Area',
            new_name='area',
        ),
    ]
