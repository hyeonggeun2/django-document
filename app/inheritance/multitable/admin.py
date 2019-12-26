from django.contrib import admin

from inheritance.multitable.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass