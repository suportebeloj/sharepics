from django.shortcuts import render
from django.views.generic import ListView
from foto.models import Imagem


# Create your views here.

class home(ListView):
    paginate_by = 10
    model = Imagem
    template_name = 'core/index.html'
    context_object_name = 'image_list'


'''
def home(request):
    return render(request, 'core/index.html')
'''
