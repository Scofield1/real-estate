# Generated by Django 4.1.2 on 2022-12-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_propertyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]