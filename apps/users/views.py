from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# from apps.quotes.models import Quote
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()


def new(req):
    return render(req, "users/home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "registration/signup.html")
    else:
        email = request.POST.get("username", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        password = request.POST.get("password", None)

        if (
            email is not None
            and password is not None
            and not User.objects.filter(email=email).exists()
        ):
            user = User(email=email, first_name=first_name, last_name=last_name)
            user.save()
            user.set_password(password)
            user.save()
            return redirect("/accounts/login")

        return render(request, "registration/signup.html")


def create(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
            return redirect("users:new")
    else:
        user = User.objects.create_user(req.POST)
        req.session["user_id"] = user.id
    return redirect("dashboard:index")


def login(req):
    valid, result = User.objects.login(req.POST)
    if not valid:
        messages.error(req, result)
        return redirect("users:new")
    else:
        req.session["user_id"] = result.id
    return redirect("quotes:index")


def logout(req):
    req.session.clear()

    return redirect("users:new")


# def edit(req, user_id):
#     if "user_id" not in req.session:
#         return redirect("users:new")

#     try:
#         context = {"user": User.objects.get(id=req.session["user_id"])}
#         print(req.POST)
#     except ObjectDoesNotExist:
#         return redirect("quotes:index")

#     return render(req, "users/edit.html", context)


def update(req, user_id):
    errors = User.objects.updateerror(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect("users:edit", user_id=user_id)
    User.objects.update(req.POST, user_id)
    return redirect("quotes:index")


def logo(req):
    return render(req, "users/logo.html")


def home(req):
    return render(req, "users/home.html")


def portfoliohome(req):
    return redirect("http://18.220.137.34/")


def edit(request, user_id=None):
    if request.method == "GET":
        return render(request, "users/edit.html")
    else:
        if user_id is None:
            request.user.first_name = request.POST["first_name"]
            request.user.last_name = request.POST["last_name"]
            request.user.save()
        return redirect("/users/home/")

