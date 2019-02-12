from django.contrib import admin
from .models import Textpage, Article, Tag, Category, Comment

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('id', 'category', 'name', 'photo_main', 'show', 'date')
  list_display_links = ('id', 'name')
  list_filter = ('show',)
  list_editable = ('show',)
  search_fields = ('name', 'description')
  list_per_page = 6

admin.site.register(Textpage)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
