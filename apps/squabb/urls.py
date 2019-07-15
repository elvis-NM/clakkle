from django.conf.urls import url
from .models import User
from apps.dashboard import views
from apps.squabb import views
from django.views.decorators.csrf import csrf_exempt

# This line is new!


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^record/$", views.record, name="record"),
    url(r"^popular/$", views.popular, name="popular"),
    url(r"^listen/$", views.listen, name="listen"),
    url(r"^yoursquabbs/$", views.yoursquabbs, name="yoursquabbs"),
    url(r"^save/audio/$", csrf_exempt(views.save_audio), name="save_audio"),
    url(r"^delete/audio/$", csrf_exempt(views.delete_audio), name="delete_audio"),
    # url(r"^view/(?P<wish_id>\d+)/$", views.view, name="view"),
    # url(r"^edit/(?P<wish_id>\d+)/$", views.edit, name="edit"),
    # url(r"^update/(?P<wish_id>\d+)/$", views.update, name="update"),
    # url(r"^delete/(?P<wish_id>\d+)/$", views.delete, name="delete"),
    # url(r"^like/(?P<wish_id>\d+)/$", views.like, name="like"),
    # url(r"^viewstats/$", views.viewstats, name="viewstats"),
]
