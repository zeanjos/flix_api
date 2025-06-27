from actors.models import Actor
from django.db import models
from genres.models import Genre


class Movie(models.Model):
    genre = models.ForeignKey(Genre,
                              on_delete=models.PROTECT,
                              related_name='movies')
    release_date = models.DateField()
    title = models.CharField(max_length=300)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.title
    