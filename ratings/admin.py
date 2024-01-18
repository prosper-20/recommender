from django.contrib import admin
from .models import Rating



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = ["user"]
    readonly_fields = ["content_object"]

# Register your models here.
