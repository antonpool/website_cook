from django.contrib.auth.models import User #импорт пользователя для подписи автора статьи
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey # строит бинарные деревья


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) #строка для ссылки
    parent = TreeForeignKey( #подкатегории (категории на mppt библиотеке)
        'self', 
        related_name='children',
        on_delete=models.SET_NULL, #при удалении удаляет все подкатегории либо нет  CASCADE()
        null=True, #не озязательное поле
        blank=True, #не обязательно при заполнении
    )


    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) #строка для ссылки

class Post(models.Model):
    autor = models.ForeignKey(
        User, #использование модели для подписи статьи этого пользователя
        related_name='posts',
        on_delete=models.CASCADE #удаление пользователя удалит все статьи? или все пометки автора
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articals')
    text: models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name = 'posts')
    cteate_at = models.DateField()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length = 50)
    pref_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name = 'recipe',
        on_delete = models.SET_NULL,
        default=0,
        null = True,
        blank = True,
    )

class Commend(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    wedsite = models.CharField(max_length=150)
    messege = models.CharField(max_length=500)
    post = models.ForeignKey( #привязка к посту
        Post,
        related_name = 'comment',
        on_delete = models.CASCADE)
