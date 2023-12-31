# Generated by Django 4.2.2 on 2023-06-26 22:44

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=300, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_published', models.BooleanField(default=False)),
                ('hits', models.BigIntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, to='category.category')),
                ('tags', models.ManyToManyField(blank=True, to='tag.tag')),
            ],
        ),
    ]
