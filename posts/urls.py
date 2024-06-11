from django.urls import path

# from django.contrib import admin
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path("admin/", include(admin.site.urls), name="admin"),
]
