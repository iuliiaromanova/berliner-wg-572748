from django import forms

from .models import Anzeige

class AnzeigeForm(forms.ModelForm):

    class Meta:
        model = Anzeige
        fields = ('title', 'image', 'zimmergroesse', 'warmmiete', 'frei_ab', 'text',)