from django.shortcuts import render, redirect

# Create your views here.


def index(req):
    return redirect("dashboard:index")


def create(req):
    return render(req, "products/ecommerce.html")


def add(req):
    return render(req, "products/moreitems.html")


def cart(req):
    return render(req, "products/shoppingcart.html")

def checkcart(req):
    return render(req, "products/cart.html")
