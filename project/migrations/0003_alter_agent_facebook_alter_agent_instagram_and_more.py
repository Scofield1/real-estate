# Generated by Django 4.1.2 on 2022-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_agent_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='agent',
            name='instagram',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='agent',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='agent',
            name='twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
