from django.contrib import admin

# Register your models here.
from . import models



admin.site.register(models.Category)
admin.site.register(models.Commend)
admin.site.register(models.Post)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)