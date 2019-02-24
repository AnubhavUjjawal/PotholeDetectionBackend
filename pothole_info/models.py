from django.db import models
from django.contrib.gis.db import models as gis
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.gis.geos import Point

# Create your models here.

class PotholeInfo(models.Model):
    """PotholeInfo model
    
    Fields:
        point -- PointField (https://docs.djangoproject.com/en/2.0/ref/contrib/gis/model-api/#pointfield)
        img -- ImageField
        userFeedback -- TextField
    """

    point = gis.PointField()
    img = models.ImageField(upload_to='pothole_info/images/')
    danger_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{str(self.id)}  => {str(self.danger_level)}'

    def save(self, *args, **kwargs):
        # print(', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        self.danger_level = kwargs['danger_level'][0]
        self.user_feedback = kwargs['user_feedback'][0]

        lat, long = map(float, kwargs['point'][0].split(','))
        self.point = Point(lat, long)
        self.img = kwargs['img'][0]
        super(PotholeInfo, self).save()