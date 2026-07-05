from django.contrib import admin
from appFacultad.models import Facultad
from appCarrera.models import Carrera


# Register your models here.

class CarreraInline(admin.TabularInline):
    model = Carrera
    extra = 0
    show_change_link = True
    
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('nombre_facultad', 'code', 'num_of_carreras')
    #search_fields = ('nombre_facultad',)
    inlines = [CarreraInline]
    def num_of_carreras(self, obj):
        return obj.carreras.count()
    num_of_carreras.short_description = 'Number of carreras'

admin.site.register(Facultad, FacultadAdmin)
