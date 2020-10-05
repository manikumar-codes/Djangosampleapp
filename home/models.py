from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122,null=True)
    password = models.CharField(max_length=122,null=True)
    address = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=12,null=True)
    zip = models.CharField(max_length=12,null=True)
    
    def __str__(self):
        return self.email
