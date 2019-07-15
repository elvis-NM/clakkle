from django.conf.urls import url
from . import views  # This line is new!


urlpatterns = [
    url(r"^home/$", views.home, name="home"),
    url(r"^new/$", views.new, name="new"),
    url(r"^create/$", views.create, name="create"),
    url(r"^login/$", views.login, name="login"),
    url(r"^signup/$", views.signup, name="signup"),
    url(r"^logout/$", views.logout, name="logout"),
    url(r"^edit/(?P<user_id>\d+)/$", views.edit, name="edit"),
    url(r"^edit/$", views.edit, name="edit"),
    url(r"^update/(?P<user_id>\d+)/$", views.update, name="update"),
    url(r"^logo/$", views.logo, name="logo"),
    url(r"^portfoliohome/$", views.portfoliohome, name="portfoliohome"),
]
