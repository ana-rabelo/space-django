# Generated by Django 5.0.2 on 2024-03-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('legenda', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=False, null=False)),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
