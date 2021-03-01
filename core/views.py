from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import ListView
from foto.models import Imagem


from .forms import SingUpForm

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


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            username = authenticate(username=user, password=pwd)
            login(request, username)
            return HttpResponseRedirect(reverse_lazy('core:home'))
    else:
        form = SingUpForm()
        return render(request, 'registration/cad_new_user.html', {
            'form': form
        })
