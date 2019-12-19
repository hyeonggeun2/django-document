from django.contrib import admin

from .models import Manufacturer, Car


# Register your models here.


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
