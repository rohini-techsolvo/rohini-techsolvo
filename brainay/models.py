from django.db import models
from django.contrib.auth.models import User


class Registeruser(models.Model):
    contact = models.CharField(max_length=30, null=True, blank=True)
    token = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)
    image = models.FileField(blank=True, upload_to="users")
    otp = models.CharField(max_length=50 ,null=True)
    connect = models.CharField(max_length=50 ,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username