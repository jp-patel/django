# Generated by Django 2.1.5 on 2021-10-28 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_author_blog_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
