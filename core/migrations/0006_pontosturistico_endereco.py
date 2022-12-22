# Generated by Django 4.1.4 on 2022-12-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_pontosturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
