from django.db import models
from django.utils import timezone
from django_bleach.models import BleachField

class Notepad(models.Model):
    notepad_title = models.Charfield(max_length=200)
    notepad_content = models.TextField()
    notepad_content = BleachField()
    notepad_published = models.DateTimeField("date published", default=datetime.now)

#OVERRIDES
    def __str__(self):
         return self.notepad_title
