from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title