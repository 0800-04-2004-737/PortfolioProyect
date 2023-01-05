from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    img = models.ImageField(upload_to="portfolio/images/", null=True, blank=True)
    url = models.URLField(blank=True)
