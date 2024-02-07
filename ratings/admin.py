from django.contrib import admin
from .models import Rating



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['content_obj', 'user', 'value', 'active']
    search_fields = ["user__username"]
    raw_id_fields = ["user"]
    readonly_fields = ["content_obj"]

# Register your models here.
