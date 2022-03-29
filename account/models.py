from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=50)
    forget_pass_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
