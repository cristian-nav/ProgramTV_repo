from django.db import models

class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.TextField()
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)