__author__ = 'Dominic Fitzgerald'
from django.conf.urls import url

urlpatterns = [
    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),
]