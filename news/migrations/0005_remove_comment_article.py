# Generated by Django 2.1.5 on 2019-02-11 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190211_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
    ]
