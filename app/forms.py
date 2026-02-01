from django import forms
from .models import Player_Serializer

class Player_Form(forms.ModelForm):
    class Meta:
        model=Player_Serializer
        field='__all__'