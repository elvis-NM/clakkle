from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return redirect("dashboard/dashboard.html")


def yourint(req):
    return render(req, "interests/yourinterests.html")


def availableint(req):
    return render(req, "interests/availableinterests.html")

