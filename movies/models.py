from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ratings.models import Rating
from django.utils import timezone
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating)
    rating_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)


    def rating_avg_display(self):
        now = timezone.now()
        if not self.rating_last_updated:
            return self.calculte_rating()
        if self.rating_last_updated > now - datetime.timedelta(minutes=1):
            return self.rating_avg
        return self.calculte_rating


    def calculte_ratings_count(self):
        return self.ratings.all().count()

    def calculate_ratings_avg(self):
        return self.ratings.all().avg()
    
    def calculte_rating(self, save=True):
        rating_avg = self.calculate_ratings_avg()
        rating_count = self.calculte_ratings_count()
        self.rating_count = rating_count
        self.rating_avg = rating_avg
        self.rating_last_updated = timezone.now()
        if save:
            self.save()
        return self.rating_avg



    def __str__(self):
        return self.title