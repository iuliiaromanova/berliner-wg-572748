from django.conf import settings
from django.db import models
from django.utils import timezone


class Anzeige(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True) #height_field = 350 , width_field = 450
    adresse = models.CharField(max_length=37, blank=True, null=True)
    zimmergroesse = models.IntegerField(default=0)
    warmmiete = models.IntegerField(default=0)
    frei_ab = models.DateField(default=timezone.now)
    text = models.TextField()
    kontakt = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  #blank=True  = pole mojet byt pustym

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
