from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    pass
