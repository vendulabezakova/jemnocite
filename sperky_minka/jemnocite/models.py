from django.db import models
from django.contrib.auth.models import User

class Difficulty(models.Model):
    difficult_list = (
        ("Easy", "Easy"),
        ("Moderate", "Moderate"),
        ("Moderately Strenuous", "Moderately Strenuous"),
        ("Strenuous", "Strenuous"),
        ("Very Strenuous", "Very Strenuous")
    )