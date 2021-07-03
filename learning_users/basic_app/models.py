from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# This part is "extending" the default user class to include additional attributes / functions

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
