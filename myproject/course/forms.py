from django import forms
from .models import Answer
class AnswerForm(forms.ModelForm):
    class Meta:
        user=Answer
        fields=['user','answer']