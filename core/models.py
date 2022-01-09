from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from os.path import join, exists
from os import remove
from datetime import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = "{0}.{1}".format(str(instance.user), filename.split(".")[-1])
    filename = 'profile_pics/user_{0}/{1}'.format(instance.user.id, filename)
    if exists(join("media", filename)):
        remove(join("media", filename))
    return filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/default_user.jpg', upload_to=user_directory_path)
    roll_number = models.CharField(max_length=50, unique=True, null=True, blank=False)
    department = models.CharField(max_length=50, null=True, blank=False)
    bus_number = models.IntegerField(null=True, blank=False)
    rfid = models.CharField(max_length=50, unique=True, null=True, blank=False, )
    is_fees_paid = models.BooleanField(default=False, null=False, blank=False)
    
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)



class Attendance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    attendance = models.CharField(max_length=8, choices=attendance_choices, default = 'present', blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=datetime.today, blank=True)

    def __str__(self):
        return "{} {}".format(self.profile.user.username, self.date.strftime("%d %b, %Y"))
        # return self.profile.user.username + 
    