from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'dealer_id', 'model_type', 'year']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
