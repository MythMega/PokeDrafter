import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image


class Tier(models.Models):
    name = models.CharField(max_length=8)
    full_name = models.CharField(max_length=32)
    level = models.PositiveIntegerField(default=0)