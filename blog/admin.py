from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin) # 管理サイトにPostモデル登録
