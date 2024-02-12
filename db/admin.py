from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models

class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 0

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ "author", 'category', 'title', 'cteate_at']
    inlines = [RecipeInLine]

@admin.register(models.Recipe)
class PostAdmin(admin.ModelAdmin):
    list_display = [ "name", 'pref_time', 'serves']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Commend)
admin.site.register(models.Tag)