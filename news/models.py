from django.db import models
from datetime import datetime
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(slug):
    new_slug = slugify(slug, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Textpage(models.Model):
    name = models.CharField(verbose_name='Page title', max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    text = models.TextField(verbose_name='Text of the page', blank=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(verbose_name='Category slug', max_length=40, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='Choose category', on_delete=models.CASCADE) # DO_NOTHING
    name = models.CharField(max_length=200, verbose_name='Title of the article', db_index=True)
    slug = models.SlugField(max_length= 220, blank = True, unique=True)
    description = models.TextField(verbose_name='Short description of the article', blank=True, db_index=True)
    text = models.TextField(verbose_name='Text of the article', blank=True, db_index=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    show = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank = True, related_name = 'articles')
    date =  models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('article_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('article_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Tag(models.Model):
    name = models.CharField(verbose_name='Name of the tag', max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['name']


class Comment(models.Model):
    name = models.CharField(verbose_name='Your name:', max_length=50)
    message = models.TextField(verbose_name='Please write your comment', blank=False)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.now, blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)
