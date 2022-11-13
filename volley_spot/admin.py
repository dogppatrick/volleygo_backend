from django.contrib import admin
from django.contrib.admin import display

from volley_spot.models import Area, Region, Gym

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("id","name", "location", "show_detail_region")
    readonly_fields = ("id",)

    @display(ordering="region",description="region_full")
    def show_detail_region(self,obj:Gym):
        return f'[{obj.region.name}][{obj.region.area.name}]'

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id","name", "show_detail_area")
    readonly_fields = ("id",)

    @display(ordering="region",description="area_name")
    def show_detail_area(self,obj:Region):
        return f'{obj.area.name}'

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("id","name",)
    readonly_fields = ("id",)


