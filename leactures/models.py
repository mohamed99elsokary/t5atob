from django.db import models
from categories import models as categories_models

# Create your models here.
class Lecture(models.Model):
    # relations
    category = models.ForeignKey(categories_models.Category, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.category.name}"
