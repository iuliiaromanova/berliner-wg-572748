from django.shortcuts import render
from django.utils import timezone
from .models import Anzeige

# Create your views here.
def anzeige_list(request):
    anzeiges = Anzeige.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'wg/anzeige_list.html', {'anzeiges': anzeiges})
