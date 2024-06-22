from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    date = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")
    original_date =  models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    picture=models.ImageField(upload_to='media/news_pictures',null=True, blank=True, verbose_name="Imagen")


    def __str__(self):
        return self.title

            