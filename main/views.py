from django.views.generic import ListView
from django.shortcuts import render
from db.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))
    # .select_related('category')
    
# def home(request):
#     return render (request, 'blog/post_list.html')

# class PostListView(ListView):
#     model = Post

#     def get_queryset(self):
#         return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')