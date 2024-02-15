from django.urls import path
from . import views


urlpatterns = [
    path ('', views.home, name = 'home'),
    path('<slug:slug>/', views.PostListView.as_view(), name = 'post_list'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailViews.as_view(), name = 'post_single')
]