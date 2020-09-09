from django import forms

from .models import Anzeige

class AnzeigeForm(forms.ModelForm):

    class Meta:
        model = Anzeige
        fields = ('title', 'image', 'adresse', 'zimmergroesse', 'warmmiete', 'frei_ab', 'text', 'kontakt',)