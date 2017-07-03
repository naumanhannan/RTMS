from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import render , redirect
from .models import VehicleCount
from rest_framework.response import Response
from rest_framework import status
from time import gmtime, strftime

def index(request):
    return HttpResponse("<h1> this is my page<h1>")

def read_file(request):
    vehicle_entrys = VehicleCount.objects.all()
    vehicle_entry = VehicleCount.objects.create()
    vehicle_entry.save()
    return render(request , 'music/show.html' , {'vehicle_entrys' : vehicle_entrys})

def alldata(APIView):
    def get(self):
        vehicle_entrys = VehicleCount.objects.all()
        serial=VehicleCountserializer(VehicleCount,many=True)
        return Response(serial.data)
        pass
    def post(self):
        pass
