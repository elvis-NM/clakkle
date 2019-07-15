from django.shortcuts import render, redirect, HttpResponse
import uuid, os
from django.conf import settings
from os import listdir, makedirs, path
from apps.squabb.models import Squabb


def index(req):
    recordings = Squabb.objects.all()
    # file_path = settings.MEDIA_ROOT + "/recordings/"
    # if not path.exists(file_path):
    #     makedirs(file_path)
    # recordings = listdir(file_path)  # models.Recordings.objects.all()
    if len(recordings) > 3:
        recordings = recordings[:3]
    ctx = {"recordings": recordings}

    return render(req, "dashboard/dashboard.html", ctx)


def fan(req):
    return render(req, "dashboard/fan.html")


def fanpage(req):
    return render(req, "dashboard/fanpage.html")


def follow(req):
    return render(req, "dashboard/follow.html")


def followingpage(req):
    return render(req, "dashboard/followingpage.html")


def sitemap(req):
    return render(req, "dashboard/sitemap.html")


def save_audio(request):
    if request.FILES:
        file = request.FILES["recording"]
        if not os.path.exists(settings.MEDIA_ROOT + "/recordings/"):
            os.makedirs(settings.MEDIA_ROOT + "/recordings/")
        file_path = settings.MEDIA_ROOT + "/recordings/" + str(uuid.uuid4()) + ".wav"
        print(file_path)
        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    return HttpResponse("Ok")
