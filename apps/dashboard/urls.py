from django.conf.urls import url
from apps.dashboard import views
from django.views.decorators.csrf import csrf_exempt

# This line is new!


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^fan/$", views.fan, name="fan"),
    url(r"^fanpage/$", views.fanpage, name="fanpage"),
    url(r"^follow/$", views.follow, name="follow"),
    url(r"^followingpage/$", views.followingpage, name="followingpage"),
    url(r"^sitemap/$", views.sitemap, name="sitemap"),
    # url(r"^save/audio/$", csrf_exempt(views.save_audio), name="save_audio"),
    # url(r"^create/$", views.create, name="create"),
    # url(r"^view/(?P<wish_id>\d+)/$", views.view, name="view"),
    # url(r"^edit/(?P<wish_id>\d+)/$", views.edit, name="edit"),
    # url(r"^update/(?P<wish_id>\d+)/$", views.update, name="update"),
    # url(r"^delete/(?P<wish_id>\d+)/$", views.delete, name="delete"),
    # url(r"^like/(?P<wish_id>\d+)/$", views.like, name="like"),
    # url(r"^viewstats/$", views.viewstats, name="viewstats"),
]
