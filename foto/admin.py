from django.contrib import admin
from .models import Imagem, Categoria


# Register your models here.
@admin.register(Imagem)
class AdminImagem(admin.ModelAdmin):
    list_display = ['titulo', 'autor']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'autor', None) is None:
            obj.autor = request.user
        obj.save()


admin.site.register(Categoria)