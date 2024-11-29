# Generated by Django 4.0 on 2024-10-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_eventbill_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcollection',
            name='method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Mobile', 'Mobile'), ('Bank', 'Bank')], default='Cash', max_length=10),
        ),
    ]