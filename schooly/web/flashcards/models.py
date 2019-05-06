from django.db import models
from django.utils import timezone

class Flashcards(models.Model)
    flashcard_title = models.Charfield(max_length=200)
    flashcard_content = models.TextField()
    num_card = models.IntegerField() 