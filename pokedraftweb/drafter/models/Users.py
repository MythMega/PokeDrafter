import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image

class User(models.Model):
    name = models.CharField(max_length=32)
    color_code = models.CharField(max_length=6, default="7f7f7f")
    profile_pic = models.ImageField(upload_to="drafter/static/drafter/media/img/profile_pic/", null=True, blank=True)
