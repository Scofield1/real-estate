# Generated by Django 4.1.2 on 2022-12-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(choices=[('Alabama', 'Alabama'), ('California', 'California'), ('Florida', 'Florida'), ('Illinois', 'Illinois'), ('New York', 'New York'), ('Texas', 'Texas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='propertystatus',
            name='status',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Sold', 'Sold'), ('Rent', 'Rent')], default='Sales', max_length=20),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='type',
            field=models.CharField(choices=[('House', 'House'), ('Office Space', 'Office Space')], default='House', max_length=20),
        ),
    ]
