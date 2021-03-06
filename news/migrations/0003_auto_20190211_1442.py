# Generated by Django 2.1.5 on 2019-02-11 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190210_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', to='news.Tag'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Choose category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, db_index=True, verbose_name='Short description of the article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Title of the article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, db_index=True, verbose_name='Text of the article'),
        ),
    ]
