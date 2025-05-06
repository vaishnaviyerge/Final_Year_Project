from django.db import models

class FreshnessPrediction(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    predicted_class = models.CharField(max_length=100, blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)
    time_taken = models.FloatField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
