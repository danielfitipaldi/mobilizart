from django.contrib import admin
from .models import Categoria

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)


admin.site.register(Categoria)
