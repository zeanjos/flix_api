from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from movies.models import Movie
class Review(models.Model):
    your_name = models.CharField(
        default='Anonimo',
        max_length = 400,
        validators=[
            MinLengthValidator(3, 
                               'Valor de caracteres menor que o permitido "(3)", coloque um valor válido.'
                                                    ),
            MaxLengthValidator(400, 
                               'Valor de caracteres maior que o permitido "(400)", coloque um valor válido.'     
                                ),
        ]
    )
    comment = models.TextField(null= True, blank= True)

    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 
                              'Valor menor do que o permitido "(0)", coloque um valor válido.'
                              ),
            MaxValueValidator(5, 
                              'Valor maior do que o permitido "(5)", coloque um valor válido.'
                              ),
        ]
    )
    

    def __str__(self):
        return str(self.movie)
