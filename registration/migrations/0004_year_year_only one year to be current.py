# Generated by Django 4.0 on 2024-10-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_committee_studentcommittee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_current', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'year',
            },
        ),
        migrations.AddConstraint(
            model_name='year',
            constraint=models.UniqueConstraint(condition=models.Q(('is_current', True)), fields=('is_current',), name='only one year to be current'),
        ),
    ]
