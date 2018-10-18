from django.db import models

# Create your models here.
class mentor_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    department_choice = (
        ('CO','Computer'),
        ('IT','InformationTechnology'),
        ('MECH','Mechanical'),
        ('EXTC','Electronics'),
    )
    department = models.CharField(max_length=4, choices=department_choice)
    image_link = models.CharField(max_length=100)
