# Generated by Django 5.0.6 on 2024-06-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='original_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='news_pictures', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
