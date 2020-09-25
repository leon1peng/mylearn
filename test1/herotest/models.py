from django.db import models


# Create your models here.

class HeroInfo(models.Model):
    """Hero"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    skill = models.CharField(max_length=128)

    # class Meta:
    #     db_table = 'heroinfo'
