from django.conf.urls import url
from .models import User
from apps.dashboard import views
from apps.products import views

# This line is new!


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^create/$", views.create, name="create"),
    url(r"^add/$", views.add, name="add"),
    url(r"^cart/$", views.cart, name="cart"),
    url(r"^checkcart/$", views.checkcart, name="checkcart"),
    # url(r"^signup/$", views.signup, name="signup"),
    # url(r"^logout/$", views.logout, name="logout")
    # url(r"^view/(?P<wish_id>\d+)/$", views.view, name="view"),
    # url(r"^edit/(?P<wish_id>\d+)/$", views.edit, name="edit"),
    # url(r"^update/(?P<wish_id>\d+)/$", views.update, name="update"),
    # url(r"^delete/(?P<wish_id>\d+)/$", views.delete, name="delete"),
    # url(r"^like/(?P<wish_id>\d+)/$", views.like, name="like"),
    # url(r"^viewstats/$", views.viewstats, name="viewstats"),
]
