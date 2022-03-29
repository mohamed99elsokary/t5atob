from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.name


class UserCatergoryLevel(models.Model):
    # relations
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    level = models.IntegerField()

    def __str__(self):
        return self.name
