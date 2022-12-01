# Generated by Django 4.1.2 on 2022-11-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('m_name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='agents')),
                ('p_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
            ],
        ),
    ]