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

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    shot = CloudinaryField('images')
    url= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    
