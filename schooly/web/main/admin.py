from django.contrib import admin
from .models import Notepad
from tinymce.widgets import TinyMCE     #for widget
from django.db import models            #overrides one of the models fields (more specifically, the TEXTFIELD)

class NotepadAdmin(admin.ModelAdmin):
    fields = ["notepad_title",
              "notepad_content",
              "notepad_published"]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Notepad, NotepadAdmin)
