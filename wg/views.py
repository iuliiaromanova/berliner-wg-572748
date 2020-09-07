from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Anzeige
from .forms import AnzeigeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def anzeige_list(request):
    anzeiges = Anzeige.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'wg/anzeige_list.html', {'anzeiges': anzeiges})

#Anzeige.objects.get(pk=pk)
def anzeige_detail(request, pk):
    anzeige = get_object_or_404(Anzeige, pk=pk)
    return render(request, 'wg/anzeige_detail.html', {'anzeige': anzeige})

@login_required
def anzeige_neue(request):
    if request.method == "POST":
        form = AnzeigeForm(request.POST, files=request.FILES)
        if form.is_valid():
            anzeige = form.save(commit=False)
            anzeige.author = request.user
            anzeige.published_date = timezone.now()
            anzeige.save()
            return redirect('anzeige_detail', pk=anzeige.pk)
    else:
        form = AnzeigeForm()
    return render(request, 'wg/anzeige_edit.html', {'form': form})

@login_required
def anzeige_edit(request, pk):
    anzeige = get_object_or_404(Anzeige, pk=pk)
    if request.method == "POST":
        form = AnzeigeForm(request.POST, files=request.FILES, instance=anzeige)
        if form.is_valid():
            anzeige = form.save(commit=False)
            anzeige.author = request.user
            anzeige.published_date = timezone.now()
            anzeige.save()
            return redirect('anzeige_detail', pk=anzeige.pk)
    else:
        form = AnzeigeForm(instance=anzeige)
    return render(request, 'wg/anzeige_edit.html', {'form': form})

@login_required
def anzeige_remove(request, pk):
    anzeige = get_object_or_404(Anzeige, pk=pk)
    anzeige.delete()
    return redirect('anzeige_list')

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            User.objects.create_user(username, password)
            return redirect(reverse("login"))

        return render(request, self.template_name)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('anzeige_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
