from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

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
    img = models.ImageField(upload_to='pothole_info/images/')
    added_on = models.DateTimeField(auto_now=True)
    danger_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{str(self.id)}  => {str(self.danger_level)}'
