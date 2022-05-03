from django.shortcuts import render
from .models import Post, Literature, GreetingAndWish


def main_page(request):
    posts = Post.objects.order_by('-created_at', '-id').all()

    context = {'title': 'karta', 'posts': posts}
    return render(request, 'main_page.html', context)


def literature(request):
    my_literature = Literature.objects.order_by('-release_year', 'author').all()
    context = {'title': 'Литература', 'my_literature': my_literature}
    return render(request, 'literature.html', context)


def greeting(request):
    greetings_and_wishes = GreetingAndWish.objects.order_by('-created_at').all()
    context = {'title': 'Приветстиве', 'greetings_and_wishes': greetings_and_wishes}
    return render(request, 'greeting.html', context)
