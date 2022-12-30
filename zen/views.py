from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View

from .models import *
from .forms import MangaForm

def home(req):
    latest_manga_list = Manga.objects.order_by('created_at')
    context = {
        "latest_manga_list": latest_manga_list,
    }
    return render(req, "index.html", context)

def read_manga(req, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    return render(req, "view_manga.html", {"manga": manga})

def create_manga(req):
    if req.method == "POST":
        form = MangaForm(req.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        context = {}

        form = MangaForm(req.POST or None)
        if form.is_valid():
            form.save()

        context["form"] = form
        return render(req, "create_manga.html", context)

def update_manga(req):
    pass

def delete_manga(req):
    pass
