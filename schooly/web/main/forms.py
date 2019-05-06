from django import forms
from app.models import Post

class NotepadForm(forms.ModelForm):
    class Meta:
        model = Notepad

        fields = ["notepad_title", "notepad_content", "notepad_published"]