from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["__str__", "calculte_ratings_count"]
    readonly_fields = ["calculte_ratings_count", "rating_avg_display"]

