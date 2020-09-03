from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Anzeige

# Create your views here.
def anzeige_list(request):
    anzeiges = Anzeige.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'wg/anzeige_list.html', {'anzeiges': anzeiges})

#Anzeige.objects.get(pk=pk)
def anzeige_detail(request, pk):
    anzeige = get_object_or_404(Anzeige, pk=pk)
    return render(request, 'wg/anzeige_detail.html', {'anzeige': anzeige})
