# from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Names(models.Model):
    name = models.CharField(max_length=32, null=False)
    location = models.PointField(srid=4326, null=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
