import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .Pokemons import Pokemon
from .Users import User
from .Tiers import Tier

class Draft(models.Model):
    pokemons = models.ManyToManyField(Pokemon, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)