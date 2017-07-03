from django.conf.urls import url
from django.contrib import admin
from . import views

from music.music_api.views import (
    VehicleCountListAPIView
)


urlpatterns = [
    url(r'^vehicle_count_json$', views.VehicleCountListAPIView.as_view()),
    url(r'^trafic_count/' ,  views.trafic_count),
    url(r'trafic_count_add/' , views.trafic_count_add_all_today),
    url(r'trafic_count_10_11' , views.trafic_count_10_11),
    url(r'add_in_rush_hours/' , views.add_in_rush_hours),
    url(r'iniciate_program/' , views.iniciate_program),
    url(r'application_ko_dyna/(?P<location_name>[A-Z0-9a-z]+)$' , views.application_ko_dyna),
    ]