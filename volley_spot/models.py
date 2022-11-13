from django.db import models
from core.models import BaseModel
# Create your models here.

class Area(BaseModel):
    name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return f'{self.name}'

class Region(BaseModel):
    name = models.CharField(max_length=128, blank=False)
    area = models.ForeignKey(Area, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}_{self.area.name}'

class Gym(BaseModel):
    name = models.CharField(max_length=128, blank=False)
    region = models.ForeignKey(Region, blank=False, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f'{self.name}'