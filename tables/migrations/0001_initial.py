# Generated by Django 5.0.6 on 2024-06-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('favorite_game', models.CharField(max_length=30, verbose_name='Juego favorito')),
            ],
        ),
        migrations.CreateModel(
            name='Game_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('max_players', models.PositiveIntegerField()),
                ('players', models.ManyToManyField(blank=True, related_name='player', to='tables.player')),
            ],
        ),
    ]
