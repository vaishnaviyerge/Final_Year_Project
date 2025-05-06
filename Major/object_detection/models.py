from django.db import models

# Create your models here.
class ObjectDetect(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    object_count = models.IntegerField(default=0, blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)