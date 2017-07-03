from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from .serializers import VehicleCountserializer
from .serializers import ExitCountserializer
from .serializers import TraficTimesSerializer
from music.models import VehicleCount
from music.models import ExitCount
from music.models import Location
from music.models import TraficTimes
from django.http import HttpResponse
import uuid
import string
import json
import threading
from datetime import datetime , timedelta 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils.timezone import datetime #important if using timezones


class VehicleCountListAPIView(ListAPIView):
	queryset = VehicleCount.objects.all()
	serializer_class = VehicleCountserializer

@api_view(['GET'])
def trafic_count(request):
	count = 0
	today = datetime.today()
	trafic_counts =  TraficTimes.objects.all()
	t_cnts = []
	data = []
	for t_c in trafic_counts :
		if (t_c.entry_count - t_c.exit_count > 15): 
			t_cnts.append(t_c)
	for t_c2 in t_cnts :
		data.append({"location": t_c2.location.location_name , "from": t_c2.start_time , "to": t_c2.end_time})
	return  Response(data)
	# serializer = TraficTimesSerializer(t_cnts, many=True)
	# return Response(serializer.data)



# ---------------------------------------from 10 AM to 11 AM 

@api_view(['GET'])
def trafic_count_10_11(request):
	arr = VehicleCount.objects.filter(entry_time__range= ("2017-06-11T10:00" , "2017-06-11T12:00") ,
	 location_id= Location.objects.get(location_name="Peco Road").id)
	arr2 = ExitCount.objects.filter(exit_time__range= ("2017-06-11T10:00" , "2017-06-11T12:00"),
	 location_id= Location.objects.get(location_name="Peco Road").id)
	if (arr.count() > 0 ):
		if request.method=="GET":
			data = {'entry_count': arr.count(),'exit_count': arr2.count() , "start_time": "2017-06-11T10:00" ,
			 "end_time": "2017-06-11T11:00" ,  "location": Location.objects.get(location_name="Peco Road").location_name}
			return Response((data))

	else:
		data = {'exists': 'No'}
		return Response(data)


@api_view(['GET'])
def trafic_count_add_all_today(request):
	all_locations = Location.objects.all()

	for loc in all_locations:
		count = 0
		arr = VehicleCount.objects.filter(entry_time__range = (datetime.now() - timedelta(minutes=12) ,
		 datetime.now()) , location_id = loc.id)
		arr2 = ExitCount.objects.filter(exit_time__range = (datetime.now() - timedelta(minutes=12) ,
		 datetime.now()) , location_id = loc.id)	
		print (arr.count())
		if (arr.count() > 0 ):	
			obj = TraficTimes(entry_count=arr.count() , exit_count= arr2.count() ,
			  start_time=datetime.now(),
			   end_time = (datetime.now() - timedelta(minutes=12) ) ,
			   location_id= loc.id)
			obj.save()
		print ("Entry Hwi")		

	# arr2 = ExitCount.objects.filter(exit_time__range= datetime.datetime.now() - datetime.timedelta(minutes=20),
	# datetime.datetime.now() - datetime.timedelta(minutes=10) ,
	# location_id= Location.objects.first().id)

	# for i in range(1,23):
	# 	arr = VehicleCount.objects.filter(entry_time__range= (str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T"+str(i)+":00" ,
	# 	 str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T"+str(i+1)+":00") ,
	# 	 location_id= Location.objects.first().id)
	# 	arr2 = ExitCount.objects.filter(exit_time__range= (str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T"+str(i)+":00" ,
	# 	 str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T"+str(i+1)+":00"),
	# 	 location_id= Location.objects.first().id)

			
	data = {"trafic count": "Job start"}
	return  Response(data)

@api_view(['GET'])
def add_in_rush_hours(request):	
	for i in range(1,23):
		arr = TraficTimes.objects.filter(start_time= (str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"T"+str(i)+":00"))


#---------------------------------------------------------


def add_in_entry_time():	
	obj = VehicleCount(location_id= Location.objects.first().id)
	obj.save()


#--------------------------------


@api_view(['GET'])
def iniciate_program(request):
	threading.Timer(10, iniciate_program(request)).start()
	add_in_entry_time()
	data = {"background": "Job start"}
	return  Response(data)


#----------------------


@api_view(['GET'])
def application_ko_dyna(request , location_name):
	loc = Location.objects.get(location_name= location_name)
	locations_filter = TraficTimes.objects.filter(location_id = loc.id)
	last_entry = locations_filter.last()

	data = "No Congestion"

	ent = last_entry.entry_count
	ext = last_entry.exit_count
	ans = ent - ext
	if (ans <= 10 ):
		data = "No Congestion"
	elif(ans > 10 and ans <= 20 ):
		data = "Medium Congestion"
	elif(ans > 20 ):
		data = "Heavy Congestion"

	res = {"Traffic": data}
	return Response(res)
	# serializer = TraficTimesSerializer(last_entry)
	# return Response(serializer.data)