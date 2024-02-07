from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["__str__", "rating_avg", "rating_count", "rating_last_upadated"]
    readonly_fields = ["rating_avg", "rating_count", "rating_avg_display"]

