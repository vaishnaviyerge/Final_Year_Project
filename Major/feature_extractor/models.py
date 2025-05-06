from django.db import models

# Create your models here.
class FeatureExtract(models.Model):

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    EAN = models.CharField(max_length=13, blank=True, null=True)
    MRP = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    manufactured_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    is_valid = models.BooleanField(default=False, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image_uploaded = models.BooleanField(default=False, blank=True, null=True)
    uploaded_image_name = models.CharField(max_length=255, blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return f'FeatureExtract {self.id}'