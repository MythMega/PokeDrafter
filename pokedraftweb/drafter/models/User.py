import math
from typing import Any
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
    xp_totale = models.BigIntegerField(default=25)

    def __str__(self) -> str:
        xp_stats = self.get_level()
        return f"{self.name} - Level {xp_stats[0]}   [ {xp_stats[1]} / {xp_stats[3]} ]"
    
    def get_level(self) -> list:
        """
        [a,b,c,d]
        a = level
        b = xp restant
        c = xp pour next level
        d = xp needed to level up 
        """
        level = 0
        xp_remain = self.xp_totale
        level_up_xp_needed = 100
        while xp_remain >= level_up_xp_needed:
            print(level, xp_remain, level_up_xp_needed-xp_remain, level_up_xp_needed)
            xp_remain = xp_remain - level_up_xp_needed
            level+=1
            level_up_xp_needed = math.ceil(level_up_xp_needed*1.008)
        print(level, xp_remain, level_up_xp_needed-xp_remain, level_up_xp_needed)
        return [level, xp_remain, level_up_xp_needed-xp_remain, level_up_xp_needed]
