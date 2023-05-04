import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .Pokemon import Pokemon

class Team(models.Model):
    pokemons = models.ManyToManyField(Pokemon, null=True, blank=True)