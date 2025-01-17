# Generated by Django 4.0 on 2024-10-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_user_options_alter_programme_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('abb', models.CharField(blank=True, max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'committee',
                'unique_together': {('name', 'abb')},
            },
        ),
        migrations.CreateModel(
            name='StudentCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_member', to='registration.committee')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_committee', to='registration.student')),
            ],
            options={
                'db_table': 'student_committee',
                'unique_together': {('student', 'committee')},
            },
        ),
    ]
