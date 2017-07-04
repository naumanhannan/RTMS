
from django.conf.urls import include, url
from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns
from music import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.url')),
    url(r'^api/', include('music.music_api.urls')),
    # url(r'^VehicleCount/',views.alldata().as_view())
]
#urlpatterns=format_suffix_patterns(urlpatterns)
