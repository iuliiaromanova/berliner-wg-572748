from django.shortcuts import render

# Create your views here.
def anzeige_list(request):
    return render(request, 'wg/anzeige_list.html', {})
