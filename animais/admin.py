from django.contrib import admin

from .models import Animal, Raca, TipoAnimal

admin.site.register([TipoAnimal, Raca, Animal])
