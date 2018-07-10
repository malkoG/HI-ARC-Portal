from django.db import models

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    class Meta:
        ordering = ('created_at', )