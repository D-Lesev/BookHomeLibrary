from django.db import models
from accounts.models import CustomUser


class NewBookCreation(models.Model):
    genre_choice = {
        ('thriller&crimes', 'Thriller and Crimes'),
        ('fantasy', 'Fantasy'),
        ('romantic', 'Romantic'),
        ('autobiography', 'Autobiography'),
        ('other', 'Other')
    }

    title = models.CharField(max_length=60)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=50, choices=genre_choice)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
