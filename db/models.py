from django.contrib.auth.models import User #импорт пользователя для подписи автора статьи
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey # строит бинарные деревья
from django.urls import reverse

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

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) #строка для ссылки

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(
        User, #использование модели для подписи статьи этого пользователя
        related_name='posts',
        on_delete=models.CASCADE #удаление пользователя удалит все статьи? или все пометки автора
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articals/')
    text = models.TextField(null = True)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name = 'posts')
    cteate_at = models.DateField()
    slug = models.SlugField(max_length=200, default='www')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug":self.slug})
    
    def get_recipes(self):
        return self.recipes.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length = 50)
    pref_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name = 'recipes',
        on_delete = models.SET_NULL,
        default=0,
        null = True,
        blank = True,
    )

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    wedsite = models.CharField(max_length=150)
    messege = models.CharField(max_length=500)
    post = models.ForeignKey( #привязка к посту
        Post,
        related_name = 'comment',
        on_delete = models.CASCADE)
   
