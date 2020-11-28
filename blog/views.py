from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'posts'
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:5]
        return posts
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'tags': Tag.objects.all().annotate(blog_count=Count('taggit_taggeditem_items')).order_by('-blog_count'),
        })
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = 'post'

class PostListView(generic.ListView):
    template_name = "post_list.html"
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return posts
    paginate_by = 20
    context_object_name = 'posts'

class NotFoundView(generic.TemplateView):
    template_name = "404.html"
    
class CategoryListView(generic.ListView):
    template_name = "category_list.html"
    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        tag = Tag.objects.get(name=tag_name)
        posts = Post.objects.filter(tags=tag, published_date__lte=timezone.now()).order_by('-published_date')
        return posts
    paginate_by = 20
    context_object_name = 'posts'
