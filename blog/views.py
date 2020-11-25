from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    template_name = "index.html"
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:5]
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = 'post'