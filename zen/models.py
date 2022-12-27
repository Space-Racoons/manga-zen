from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Status(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Manga(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    views = models.IntegerField()
    description = models.CharField(max_length=3000)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    ch_number = models.IntegerField()
    image_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ch_number}, {self.manga.title[:10]}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.content[:10]}'
