from django.db import models
import PIL
# Create your models here.


class NewImage(models.Model):
    width = models.IntegerField(default='')
    height = models.IntegerField(default='')
    image = models.ImageField(default='',
                              width_field='width',
                              height_field='height')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    old_width = models.IntegerField(null=True)
    old_height = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
