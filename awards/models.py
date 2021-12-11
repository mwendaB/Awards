from django.db import models
from django.contrib.auth.models import User
from cloudinary import CloudinaryField



class Profile(models.Model):
    photo = CloudinaryField('images')
    bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    datecreated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    
