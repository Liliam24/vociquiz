from django.shortcuts import render
from django.http import HttpResponse

from .models import Vocabulary

# Create your views here.
def index(request):
    vocabularies = Vocabulary.objects.all()
    context = {
        'vocabularies': vocabularies
    }
    return render(request, 'vociquizapp/index.html', context)

def menu(request, vocabulary_id):

    return HttpResponse("Das ist das Menu!")
