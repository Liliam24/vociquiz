from django.shortcuts import render

from .models import Vocabulary

# Create your views here.
def index(request):
    vocabularies = Vocabulary.objects.all()
    context = {
        'vocabularies': vocabularies
    }
    return render(request, 'vociquizapp/index.html', context)

def menu(request, vocabulary_id):

    context = {
        
    }
    return render(request, 'vociquizapp/menu.html', context)
