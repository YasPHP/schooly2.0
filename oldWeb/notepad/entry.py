from django.db import models

class Notepad(models.Model):
    note_title = models.CharField(max_length=200)

class Entry(models.Model):
    note = models.ForeignKey(note_title)
    title = models.CharField(max_length=200)
    body = models.TextField()
    note_date = models.DateTimeField(default=timezone.now)

    #query it like django
    Entry.filter(note_name= input)

    def __str__(self):
        return self.note

