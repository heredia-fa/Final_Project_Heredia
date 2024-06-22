from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game_table(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre de la mesa:")
    game = models.CharField(max_length=20, verbose_name="Juego:")
    description = models.TextField(verbose_name="Descripcion")
    date=models.DateTimeField(verbose_name="Fecha")
    players = models.ManyToManyField('Player', related_name='player', blank=True)
    max_players = models.PositiveIntegerField(verbose_name="Cantidad de Jugadores")
    

    def __str__(self):
        return self.name

    def add_player(self, player):
        self.players.add(player)

    def free_places(self):
       cant= self.max_players - self.players.count()
       return cant
    
    class Meta:
        verbose_name = 'Mesa de juego'
        verbose_name_plural = 'Mesas de juego'
    


class Player(models.Model):

    name = models.CharField(max_length=30, verbose_name= "Nombre")
    lastname = models.CharField(max_length=30, verbose_name= "Apellido")
    email = models.EmailField()
    age= models.IntegerField(verbose_name="Edad")
    favorite_game = models.CharField(max_length=30, verbose_name="Juego favorito")
    player_picture = models.ImageField(upload_to='player_picture',null=True, blank=True, verbose_name="Imagen")
    #user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.lastname}"
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'