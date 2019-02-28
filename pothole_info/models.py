import requests

from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models
from django.db.models.signals import post_save
from io import BytesIO
from PIL import Image

# Create your models here.

class PotholeInfo(models.Model):
    """PotholeInfo model
    
    Fields:
        lat, long -- Latitude and Longitude
        img -- ImageField
        userFeedback -- TextField
    """

    lat  = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    img = models.ImageField(upload_to='pothole_info/images/img')
    img_with_potholes = models.ImageField(upload_to='pothole_info/images/img_with_potholes',
                            null=True, blank=True)
    added_on = models.DateTimeField(auto_now=True)
    danger_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{str(self.id)}  => {str(self.danger_level)}'

    def get_image_with_pothole_path(self):
        path = str(self.img.path)
        path = path.replace('/img/', '/img_with_potholes/')
        return path
    
    def get_image_with_pothole_name(self):
        path = str(self.img.name)
        path = path.replace('/img/', '/img_with_potholes/')
        return path

    @classmethod
    def create_img_with_potholes(cls, instance, content):
        path = instance.get_image_with_pothole_path()
        f = open(path, 'wb')
        f.write(content)
        f.close()
        return open(path, 'rb')

    @classmethod
    def add_image_with_potholes(cls, sender, instance, **kwargs):
        try:
            """Adds img_with_potholes_for_image before saving the image"""
            headers = {'enctype': 'multipart/form-data'}
            # print(instance.img.path, instance.img.name)
            r = requests.post(settings.TF_SERVER,
                    files={"pothole": open(instance.img.path, 'rb')})
            file = PotholeInfo.create_img_with_potholes(instance, r.content)
            f_name = instance.get_image_with_pothole_name()
            PotholeInfo.objects.filter(pk=instance.pk).update(img_with_potholes=File(file, name=f_name))
            file.close()
        except Exception:
            pass
        
        


post_save.connect(PotholeInfo.add_image_with_potholes, sender=PotholeInfo)

