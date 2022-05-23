from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.views.generic import UpdateView

from .forms.auth import AuthForm
from .forms.profile_form import ProfileForm
from .models import Post
from .forms.registration_form import RegistrationForm


class RegistrationPage(View):
    @staticmethod
    def post(request):

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            "reg_form": form,
        }
        return render(request, 'registration_page.html', context)

    @staticmethod
    def get(request):
        form = RegistrationForm
        context = {
            "reg_form": form,
        }
        return render(request, 'registration_page.html', context)


class MainPage(View):
    @staticmethod
    def get(request):
        posts = Post.objects.order_by('-created_at', '-id').all()

        context = {'title': 'karta', 'posts': posts}
        return render(request, 'main_page.html', context)


class AuthPage(View):
    @staticmethod
    def post(request):
        form = AuthForm(request.POST)
        error = False

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user is not None:
                auth.login(request, user)

                next_page = request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        context = {
            "auth_form": form,
            "error": error
        }
        return render(request, 'auth_page.html', context)

    @staticmethod
    def get(request):
        form = AuthForm
        context = {
            "auth_form": form,
        }
        return render(request, 'auth_page.html', context)


class ProfilePage(View):
    @staticmethod
    def get(request):
        form = ProfileForm
        context = {"profile_form": form}
        return render(request, 'profile_page.html', context)

    @staticmethod
    def post(request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

            redirect('/profile/')

        context = {"profile_form": form}
        return render(request, 'profile_page.html', context)


class ProfileUpdate(ProfilePage, UpdateView):
    pass
