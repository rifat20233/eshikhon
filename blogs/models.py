from django.db import models

# Create your models here.
class Blogtable(models.Model):
    subject = models.CharField(max_length=255,null=False,blank=False)
    content = models.TextField(null=False,blank=False)