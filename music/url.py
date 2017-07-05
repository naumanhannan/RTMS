from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    #url(r'read_file' , views.read_file),
    url(r'read_file' , views.read_file),
    url(r'exit_file' , views.exit_file),


]
