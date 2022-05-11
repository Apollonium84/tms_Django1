from django.shortcuts import render, redirect
from .forms.authorization import AuthorizationForm
from .forms.registration import RegistrationForm
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


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm

    context = {
        "reg_form": form,
    }
    return render(request, 'registration_page.html', context)


# def authorization_page(request):
#     if request.method == "POST":
#         form = AuthorizationForm(request.POST)
#         if form.is_valid():
#             return redirect('/')
#     else:
#         form = AuthorizationForm
#
#     context = {
#         "auth_form": form,
#     }
#     return render(request, 'authorization_page.html', context)
