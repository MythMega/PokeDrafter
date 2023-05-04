import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .Pokemons import Pokemon

class Set(models.Model):
    custom_name = models.CharField(max_length=24)
    poke = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    ability = models.CharField(max_length=32)
    move_a = models.CharField(max_length=32)
    move_b = models.CharField(max_length=32)
    move_c = models.CharField(max_length=32)
    move_d = models.CharField(max_length=32)
    tera_type = models.CharField(max_length=32)
    nature = models.CharField(max_length=32)
    item = models.CharField(max_length=32)
    ev_Hp = models.IntegerField(default=0)
    ev_Atk = models.IntegerField(default=0)
    ev_Def = models.IntegerField(default=0)
    ev_SpA = models.IntegerField(default=0)
    ev_SpD = models.IntegerField(default=0)
    ev_Spe = models.IntegerField(default=0)
    level = models.IntegerField(default=100)
    iv_Hp = models.IntegerField(default=31)
    iv_Atk = models.IntegerField(default=31)
    iv_Def = models.IntegerField(default=31)
    iv_SpA = models.IntegerField(default=31)
    iv_SpD = models.IntegerField(default=31)
    iv_Spe = models.IntegerField(default=31)


    def generate_set(self) -> str:
        #exemple :
        #
        #pota (Azumarill) @ Sitrus Berry  
        # Ability: Huge Power  
        # Level: 87  
        # Tera Type: Dark  
        # EVs: 108 HP / 60 Atk / 4 Def / 40 SpA / 28 SpD / 100 Spe  
        # Adamant Nature  
        # IVs: 23 HP / 26 Atk / 20 Def / 25 SpA / 24 SpD / 23 Spe  
        # - Belly Drum  
        # - Play Rough  
        # - Aqua Jet  
        # - Liquidation

        result = ""
        result += f"{self.name} ({self.poke}) @ {self.item}\n"
        result += f"Ability: {self.ability}\n"
        result += f"Level: {self.level}\nTera Type: {self.tera_type}\n"
        result += f"EVs: {self.ev_Hp} / {self.ev_Atk} / {self.ev_Def} / {self.ev_SpA} / {self.ev_SpD} / {self.ev_Spe}\n"
        result += f"{self.nature} Nature\n"
        result += f"IVs: {self.iv_Hp} / {self.iv_Atk} / {self.iv_Def} / {self.iv_SpA} / {self.iv_SpD} / {self.iv_Spe}\n"
        result += f"- {self.move_a}\n- {self.move_b}\n- {self.move_c}\n- {self.move_d}\n"
        
        return result
