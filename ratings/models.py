from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.db.models.signals import post_save
from django.utils import timezone

User = get_user_model()

class RatingChoice(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE =5
    __empty__ = "Rate this"


class RatingQuerySet(models.QuerySet):
    def avg(self):
        return self.aggregate(average=Avg('value'))['average']

class RatingManager(models.Manager):
    def get_queryset(self):
        return RatingQuerySet(self.model, using=self.db)

    def avg(self):
        return self.get_queryset().avg()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True, choices=RatingChoice.choices)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_obj = GenericForeignKey("content_type", "object_id")
    active = models.BooleanField(default=True)
    active_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = RatingManager()


    class Meta:
        ordering = ["-timestamp"]




def rating_post_save(sender, instance, created, *args, **kwargs):
    if created:
        _id = instance.id
        if instance.active:
            qs = Rating.objects.filter(
                content_type = instance.content_type, 
                object_id = instance.object_id,
                user=instance.user
            ).exclude(id=_id, active=False)
            qs.update(active=False, active_update_timestamp=timezone.now())
            


post_save.connect(rating_post_save, sender=Rating)



