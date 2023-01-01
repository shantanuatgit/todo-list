from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEGORY = (
    ("personal", "personal"),
    ("shopping", "shopping"),
    ("wishlist", "wishlist"),
    ("work", "work"),
)

class Task(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY, default="personal")
    topic = models.CharField(max_length=225)
    desciption = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)