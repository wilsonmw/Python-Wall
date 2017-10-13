from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^postmessage$', views.postmessage),
    url(r'^postcomment$', views.postcomment),
    url(r'^stickypost$', views.stickypost),
]