from django.shortcuts import render, redirect
from os import listdir, makedirs, path
from django.conf import settings
from django.shortcuts import HttpResponse
from .models import Squabb
import uuid
import os
from apps.users.models import User


def index(req):
    return redirect("dashboard/dashboard.html")


def record(req):
    return render(req, "squabb/recordsquabb.html")


def listen(req):
    return render(req, "squabb/listensquabb.html")


def popular(req):
    return render(req, "squabb/popularsquabbles.html")


def yoursquabbs(request):
    recordings = Squabb.objects.filter(creator=request.user)

    # file_path = settings.MEDIA_ROOT + "/recordings/"
    # if not path.exists(file_path):
    #     makedirs(file_path)
    # recordings = listdir(file_path)  # models.Recordings.objects.all()
    ctx = {
        'recordings': recordings
    }
    return render(request, "squabb/yoursquabbles.html", ctx)


def delete_audio(request):
    if request.method == 'GET' and request.GET.get('id', None) is not None:
        squabb = Squabb.objects.get(pk=request.GET.get('id'))
        file_path = settings.MEDIA_ROOT + squabb.voicefile.name
        squabb.delete()
        os.remove(file_path)

    return redirect('/')


def save_audio(request):
    if request.FILES:
        file_name = "/recordings/"+str(uuid.uuid4())+'.wav'
        file = request.FILES['recording']
        if not os.path.exists(settings.MEDIA_ROOT+"/recordings/"):
            os.makedirs(settings.MEDIA_ROOT+"/recordings/")
        file_path = settings.MEDIA_ROOT+file_name
        print(file_path)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        squabb = Squabb(
            voicefile=file_name,
            content='',
            creator=request.user
        )
        squabb.save()
    # voicefile = models.FileField()
    # content = models.CharField(max_length=255)
    # creator = models.ForeignKey(User, related_name="squabbs")
    # users_liked = models.ManyToManyField(User, related_name="liked_squabbs")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    return HttpResponse("Ok")
