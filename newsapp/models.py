from django.db import models
from django.core.validators import MinValueValidator


class NewsModel(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()
    author = models.CharField(
        max_length=50,
            )
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
