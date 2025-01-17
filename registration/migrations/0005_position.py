# Generated by Django 4.0 on 2024-10-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_year_year_only one year to be current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'position',
            },
        ),
    ]
