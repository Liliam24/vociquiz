from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

class Word(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Attempt(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    success = models.BooleanField()