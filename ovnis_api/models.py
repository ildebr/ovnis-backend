from django.db import models
import uuid
from opencage.geocoder import OpenCageGeocode
from django.db.models.signals import pre_save, post_save
from django.conf import settings
import datetime
# Create your models here.

apikey= "31bb7130af364a82a6b18651213d2dc7"
geocoder = OpenCageGeocode(apikey)

class Sighting(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=400, default="")
    latitude = models.DecimalField(max_digits=22 , decimal_places=16)
    longitude = models.DecimalField(max_digits=22 , decimal_places=16)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, blank=True, null=True)
    continent = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=300, default="", null=True, blank=True)



    def __str__(self):
        return f'id: {self.id} date: {self.date}'

def sighting_pre_save(sender, instance,*args, **kwargs):

    if instance.latitude and not instance.country:
        results = geocoder.reverse_geocode(instance.latitude, instance.longitude)
        print(results[0])

        instance.country = results[0]['components']['country']
        instance.continent = results[0]['components']['continent']

pre_save.connect(sighting_pre_save, sender=Sighting)

class Comment(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=300)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']