from django.db import models
from film.models import Film
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    film = models.ForeignKey(Film, on_delete=models.CASCADE,related_name='film_id')

    class Meta:
        unique_together = ('user', 'film')