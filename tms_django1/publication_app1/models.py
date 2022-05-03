from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.CharField(max_length=2056, blank=False, null=False)


class Literature(models.Model):
    author = models.CharField(max_length=256, unique=False, blank=False, null=False)
    work = models.CharField(max_length=256, unique=False, blank=False, null=False)
    release_year = models.IntegerField(blank=False, null=False)


class GreetingAndWish(models.Model):
    greeting = models.CharField(max_length=256, unique=False, blank=False, null=False)
    wish = models.CharField(max_length=256, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
