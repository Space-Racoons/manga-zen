from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    # TODO(felipe): Checar melhor maneira de lidar com passwords em django. Quase
    # certeza que isso não é recomendado.
    hashed_password = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Manga(models.Model):
    # NOTE(felipe): I don't think there is a reason for mangas and users have a relation
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=200)
    # NOTE(felipe): What is this exactly? is stuff like ongoing/finished/yato? If so,
    # we should probably do the same we did with the attribute genre.
    status = models.CharField(max_length=50)
    views = models.IntegerField()
    description = models.CharField(max_length=3000)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    ch_number = models.IntegerField()
    image_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # NOTE(felipe): If the user is deleted, sure we want to delete all his comments?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
