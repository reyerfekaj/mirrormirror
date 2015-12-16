from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    transcript = models.TextField(blank=True, default="")
    speech = models.TextField(blank=True, default="")
    feedback = models.TextField(blank=True, default="")

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
