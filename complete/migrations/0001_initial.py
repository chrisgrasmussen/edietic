# Generated by Django 5.0.6 on 2024-09-17 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('start', '0004_delete_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('complete_timestamp', models.DateTimeField(auto_now_add=True)),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.start')),
            ],
            options={
                'verbose_name': 'Complete',
                'verbose_name_plural': 'Completes',
                'ordering': ('-complete_timestamp',),
            },
        ),
    ]
