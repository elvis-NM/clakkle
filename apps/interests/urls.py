from django.conf.urls import url
from apps.dashboard import views
from apps.interests import views

# This line is new!


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^availableint/$", views.availableint, name="availableint"),
    url(r"^yourint/$", views.yourint, name="yourint")
    # url(r"^create/$", views.create, name="create"),
    # url(r"^view/(?P<wish_id>\d+)/$", views.view, name="view"),
    # url(r"^edit/(?P<wish_id>\d+)/$", views.edit, name="edit"),
    # url(r"^update/(?P<wish_id>\d+)/$", views.update, name="update"),
    # url(r"^delete/(?P<wish_id>\d+)/$", views.delete, name="delete"),
    # url(r"^like/(?P<wish_id>\d+)/$", views.like, name="like"),
    # url(r"^viewstats/$", views.viewstats, name="viewstats"),
]
