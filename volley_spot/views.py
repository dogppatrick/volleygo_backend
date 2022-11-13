from django.shortcuts import render

from core.views import BaseCreateView
from volley_spot.models import Area, Gym, Region
from volley_spot.serializers import GymSerializer, RegionSerializer, AreaSerializer


class GymAPI(BaseCreateView):
    model_class = Gym
    queryset = model_class.objects.all()
    serializer_class = GymSerializer


class RegionAPI(BaseCreateView):
    model_class = Region
    queryset = model_class.objects.all()
    serializer_class = RegionSerializer


class AreaAPI(BaseCreateView):
    model_class = Area
    queryset = model_class.objects.all()
    serializer_class = AreaSerializer
