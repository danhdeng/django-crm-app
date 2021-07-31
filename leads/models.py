from django.db import models

# Create your models here.
class SalesPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)



class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_image = models.ImageField(blank=True, null=True)
    special_file = models.FileField(blank=True, null=True)
    phoned= models.BooleanField(default=False)
    agent = models.ForeignKey("SalesPerson", on_delete=models.CASCADE)