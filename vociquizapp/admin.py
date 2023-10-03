from django.contrib import admin
from .models import Vocabulary, Word, Attempt

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(Word)
admin.site.register(Attempt)
