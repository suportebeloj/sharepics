from django.shortcuts import render
from django.views.generic import ListView
from foto.models import Imagem
from random import choice


# Create your views here.

class home(ListView):
    paginate_by = 10
    model = Imagem
    template_name = 'core/index.html'
    context_object_name = 'image_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        img = Imagem.objects.all()
        context['banner'] = choice(img)
        return context


