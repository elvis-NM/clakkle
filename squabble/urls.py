"""squabble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^squabble/products/", include("apps.products.urls", namespace="products")),
    url(r"^squabble/squabb/", include("apps.squabb.urls", namespace="squabb")),
    url(r"^squabble/interests/", include("apps.interests.urls", namespace="interests")),
    url(r"^users/", include("apps.users.urls", namespace="users")),
    url("accounts/", include("django.contrib.auth.urls")),
    url(r"^", include("apps.dashboard.urls", namespace="dashboard")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
