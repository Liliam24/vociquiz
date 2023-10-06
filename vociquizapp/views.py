from django.shortcuts import render
import random
from .models import Vocabulary, Word

# Create your views here.
def index(request):
    vocabularies = Vocabulary.objects.all()
    context = {
        'vocabularies': vocabularies
    }
    return render(request, 'vociquizapp/index.html', context)

def menu(request, vocabulary_id):

    context = { "vocabulary_id": vocabulary_id
    
        
    }
    return render(request, 'vociquizapp/menu.html', context)

def vocicard(request, vocabulary_id):
    words = Word.objects.filter(vocabulary__pk=vocabulary_id)
    random_word = random.choice(list(words))
   
    context = { "random_word": random_word, 
    "vocabulary_id": vocabulary_id
        
    }
    return render(request, 'vociquizapp/vocicard.html', context)
