import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .Tier import Tier


class Pokemon(models.Model):
    name = models.CharField(max_length=32)
    form = models.CharField(max_length=23, null=True, blank=True, default=None)
    sprite = models.ImageField(upload_to="drafter/static/drafter/media/img/poke_pic/", null=True, blank=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    numero = models.IntegerField(null=True)

    def __str__(self) -> str:
        result = f"[{self.tier}] - {self.numero} {self.name}"
        if self.form is not None:
            result += f"({self.form})"
