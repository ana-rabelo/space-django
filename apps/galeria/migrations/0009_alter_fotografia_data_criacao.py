# Generated by Django 5.0.2 on 2024-03-16 13:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
