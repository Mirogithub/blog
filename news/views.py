from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Textpage, Article, Category, Tag, Comment
from .newsmixin import *
from .forms import ArticleForm, TagForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def showlist(request):
    return redirect('articlelist_url')

def textpage(request, slug):
    obj = get_object_or_404(Textpage, slug=slug)
    return render(request, 'news/index.html', {'textpage': obj})

def article_list(request):
    title = "All articles"
    articles = Article.objects.filter(show = True)
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    context = {
        'title': title,
        'articles': page,
        'is_paginated': is_paginated,
    }
    return render(request, 'news/article_list.html', context)

def article_cat_list(request, slug):
    articles = Article.objects.order_by('-date').filter(show=True, category__slug__iexact=slug)
    category = Category.objects.get(slug__iexact=slug)
    title = "Articles by category" + category.name
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    context = {
        'title': title,
        'articles': page,
        'is_paginated': is_paginated,
    }
    return render(request, 'news/article_list.html', context)

def article_tag_list(request, id):
    articles = Article.objects.order_by('name').filter(show=True, tags__id=id)[:15]
    tag = Tag.objects.get(id=3)
    title = "Articles with the tag" + tag.name

    context = {
        'title': title,
        'articles': articles,
    }
    return render(request, 'news/article_list.html', context)


class ArticleDetail(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        comments = Comment.objects.order_by('-date').filter(show=True, article = article.id)
        latest_articles = Article.objects.filter(show = True).order_by('-date')[:3]
        return render(request, 'news/article_view.html', context={'article':article,
                                                        'latest_articles': latest_articles,
                                                        'comments': comments,})


class ArticleCreate(LoginRequiredMixin, ObjectCreatMixin, View):
    model_form = ArticleForm
    template = 'news/article_create_form.html'


class ArticleUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Article
    model_form = ArticleForm
    template = 'news/article_update_form.html'


class ArticleDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Article
    template = 'news/article_delete_form.html'
    redirect_url= 'articlelist_url'

@login_required(login_url='/accounts/login/')
def tag_list(request):
    title = "List of tags"
    tags = Tag.objects.all().order_by('name')

    context = {
        'title': title,
        'tags': tags,
    }
    return render(request, 'news/tag_list.html', context)


class TagCreate(LoginRequiredMixin, ObjectCreatMixin, View):
    model_form = TagForm
    redirect_url= 'taglist_url'
    template = 'news/tag_create_form.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    redirect_url= 'taglist_url'
    template = 'news/tag_update_form.html'

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    redirect_url= 'taglist_url'


def comment_add(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('name') and request.POST.get('message'):
            comment = Comment(name= request.POST.get('name'),
                            message= request.POST.get('message'),
                            article=Article.objects.get(pk = request.POST.get('article_id'))).save()
            return redirect(reverse('article_detail_url', kwargs={'slug': request.POST.get('article_slug')}))
