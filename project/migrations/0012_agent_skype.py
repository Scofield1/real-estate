# Generated by Django 4.1.2 on 2022-12-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_remove_propertyamenity_amenities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='skype',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
