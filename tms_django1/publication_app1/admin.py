from django.contrib import admin
from .models import Post, Literature, GreetingAndWish


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)


@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'work', 'release_year']
    ordering = ('-release_year', '-id')


@admin.register(GreetingAndWish)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'greeting', 'wish', 'created_at']
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)
