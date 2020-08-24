from django.conf import settings
from django.db import models
from django.utils import timezone


class Anzeige(models.Model):
    #autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #bezirk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zimmergröße = models.IntegerField(default=0)
    warmmiete = models.IntegerField(default=0)
    frei_ab = models.DateField(default=timezone.now)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  #blank=True  = pole mojet byt pustym

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
