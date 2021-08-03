from django.contrib import admin
from rango.models import City, Scenery
from rango.models import UserProfile

class SceneryAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'url')

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(City, CityAdmin)
admin.site.register(Scenery, SceneryAdmin)
admin.site.register(UserProfile)