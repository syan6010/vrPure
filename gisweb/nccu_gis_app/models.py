from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class imgData(models.Model):	
    title = models.CharField(max_length=60, null=False, default = "")	
    content = models.TextField(null=False, default = "")	
    type = models.CharField(max_length=20, null=False, default = "")
    purl = models.CharField(max_length=100, null=False, default = "")
    create_at =  models.DateTimeField(auto_now_add=True)	
    lon = models.CharField(max_length=20, null=False, default = "")
    lat = models.CharField(max_length=20, null=False, default = "")
    username = models.CharField(max_length=150 , null=False, default = "")	

    def __str__(self):		
        return self.title	


class markerType(models.Model):	
    title = models.CharField(max_length=60, null=False, default = "")	

    def __str__(self):		
        return self.title	