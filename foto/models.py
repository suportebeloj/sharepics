from django.db import models
from users.models import CustomUser


# Create your models here.
class Imagem(models.Model):
    titulo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='album/%Y/%m/%d')
    descricao = models.TextField(blank=True)
    carregada_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('-titulo',)
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome