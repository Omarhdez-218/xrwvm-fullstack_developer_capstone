from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'year']
    inlines = CarModelInline

class CarMakeAdmin(CarModelInline):
    ...

# Register models here
