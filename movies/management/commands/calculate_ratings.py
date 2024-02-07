from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from cfehome import utils as cfehome_utils
from movies.models import Movie
from movies.tasks import task_calculate_movie_ratings
from ratings.models import Rating


User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("--all", action="store_true", default=False)


    def handle(self, *args, **options):
        all = options.get('all')
        task_calculate_movie_ratings(all=all)
