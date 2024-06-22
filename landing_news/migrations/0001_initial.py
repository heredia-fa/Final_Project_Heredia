# Generated by Django 5.0.6 on 2024-06-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
                ('original_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='news_pictures', verbose_name='Imagen')),
            ],
        ),
    ]
