# Generated by Django 5.0.3 on 2024-04-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0002_rename_catetory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
