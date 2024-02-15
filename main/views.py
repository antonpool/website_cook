from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from db.models import Post
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    context_object_name = "post_list" #название в шаблоне
    template_name = "db/post_lis.html" #файл html шаблон

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))
    # .select_related('category')
    
class PostDetailViews(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "db/single-post.html"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context



def home (request):
    return render (request, 'base.html')

