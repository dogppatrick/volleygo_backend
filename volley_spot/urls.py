from django.urls import path
from volley_spot.views import GymAPI, RegionAPI, AreaAPI

urlpatterns = [
    path(route='gym', view=GymAPI.as_view(), name="gym"),
    path(route='area', view=AreaAPI.as_view(), name="area"),
    path(route='region', view=RegionAPI.as_view(), name="region"),
]