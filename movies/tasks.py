from .models import Movie

def task_calculate_movie_ratings(all=False):
    qs = Movie.objects.needs_updating()
    if all:
        qs = Movie.objects.all()
    for obj in qs:
        obj.calculte_rating(save=True)
# def task_calculate_movie_rating_all():
#     qs = Movie.objects.all()
#     for obj in qs:
#         obj.calculte_rating(save=True)



# def task_calculate_movie_rating_needs_updating():
#     qs = Movie.objects.needs_updating()
#     for obj in qs:
#         obj.calculte_rating(save=True)