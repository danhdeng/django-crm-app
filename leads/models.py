from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save



# Create your models here.

class User(AbstractUser):
    is_organizer=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)
    
class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self)->str:
        return self.user.username
    
class SalesPerson(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    organization= models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self)->str:
        return f"{self.user.username} {self.user.email}"

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_image = models.ImageField(blank=True, null=True)
    special_file = models.FileField(blank=True, null=True)
    phoned= models.BooleanField(default=False)
    age =models.IntegerField(default=0)
    agent = models.ForeignKey("SalesPerson", null=True, blank=True, on_delete=models.SET_NULL)
    organization= models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"frist name: {self.first_name} last name: {self.last_name}"
    
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

    