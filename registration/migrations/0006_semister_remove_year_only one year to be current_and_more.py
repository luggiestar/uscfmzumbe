# Generated by Django 4.0 on 2024-10-26 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Semister 1', 'Semister 1'), ('Semister 2', 'Semister 2')], max_length=40)),
                ('is_current', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'semister',
            },
        ),
        migrations.RemoveConstraint(
            model_name='year',
            name='only one year to be current',
        ),
        migrations.RemoveField(
            model_name='year',
            name='is_current',
        ),
        migrations.AlterField(
            model_name='year',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterModelTable(
            name='year',
            table=None,
        ),
        migrations.AddField(
            model_name='semister',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.year'),
        ),
        migrations.AddConstraint(
            model_name='semister',
            constraint=models.UniqueConstraint(condition=models.Q(('is_current', True)), fields=('is_current',), name='only one semister can be current'),
        ),
    ]