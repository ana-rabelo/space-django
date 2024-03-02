# Generated by Django 5.0.2 on 2024-03-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta'), ('OUTRO', 'Outro')], default='Outro', max_length=50),
        ),
    ]
