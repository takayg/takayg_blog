from django.db import models
from django.conf import settings
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = MarkdownxField('Contents', help_text='To Write with Markdown format')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager(blank=True) 

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.title
    
    def formatted_markdown(self):
        return markdownify(self.text)