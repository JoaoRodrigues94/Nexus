from django.contrib import admin
from core.models import Albuns
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_album','artista', 'genero')

admin.site.register(Albuns, AlbumAdmin) #Cadastro do banco de dados.