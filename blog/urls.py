from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('404/', views.NotFoundView.as_view()),
    path('category/<str:tag_name>', views.CategoryListView.as_view(), name='category'),
]