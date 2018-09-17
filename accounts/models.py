from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

DEFAULT = 'img/default.jpg'
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=400, default='')
    interests = models.CharField(max_length=200, default='')
    picture = models.ImageField(upload_to='profile_picture', default=DEFAULT)

    def __str__(self):
        return self.user.username
def create_profile(sender, **kwargs):
    if(kwargs['created']):
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)