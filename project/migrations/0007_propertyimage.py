# Generated by Django 4.1.2 on 2022-12-01 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_property_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.property')),
            ],
        ),
    ]