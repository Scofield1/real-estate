from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(default='media/profile_pic.svg', upload_to='profile')

    def __str__(self):
        return self.user.username