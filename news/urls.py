from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.showlist, name='showlist_url'),
    path('textpage/<str:slug>/', views.textpage, name='textpage_url'),
    path('articles/', views.article_list, name='articlelist_url'),
    path ('articles/category/<str:slug>/', views.article_cat_list, name='article_cat_list_url'),
    path ('articles/tag/<int:id>/', views.article_tag_list, name='article_tag_list_url'),
    path ('articles/<str:slug>/', ArticleDetail.as_view(), name='article_detail_url'),
    path ('manage/create_article/', ArticleCreate.as_view(), name='article_create_url'),
    path ('manage/update_article/<str:slug>', ArticleUpdate.as_view(), name='article_update_url'),
    path ('manage/delete_article/<str:slug>/', ArticleDelete.as_view(), name='article_delete_url'),

    path ('tags/', views.tag_list, name='taglist_url'),
    path ('manage/create_tag/', TagCreate.as_view(), name='tag_create_url'),
    path ('manage/update_tag/<str:slug>/', TagUpdate.as_view(), name='tag_update_url'),
    path ('manage/delete_tag/<str:slug>/', TagDelete.as_view(), name='tag_delete_url'),

    path ('comment_add/', views.comment_add, name='comment_add_url'),
    # path ('news/<str:news_cat>/', views.newscat, name='newscat_url'),
    # path ('news/newsdetail/<int:id>/', NewsDetail.as_view(), name='newsdetail_url'),
    # path ('articles/articledetail/<int:id>/', ArticleDetail.as_view(), name='articledetail_url'),
    # path('articles/', views.articleslist, name='articleslist_url'),
    # path('articles/<str:articles_cat>/', views.articlescat, name='articlescat_url'),
    # path ('editarticles/create/', ArticlesCreate.as_view(), name='article_create_url'),
    # path ('editarticles/update/<int:id>', ArticlesUpdate.as_view(), name='article_update_url'),
    # path ('editarticles/delete/', ArticlesDelete.as_view(), name='article_delete_url'),
]
