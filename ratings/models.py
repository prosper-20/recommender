from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()

class RatingChoice(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE =5
    __empty__ = "Rate this"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True, choices=RatingChoice.choices)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_obj = GenericForeignKey("content_type", "object_id")
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

