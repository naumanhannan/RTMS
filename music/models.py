from django.db import models


class Location(models.Model):
	location_name =models.CharField(max_length=255)
	def __str__(self):
	  	return self.location_name

class VehicleCount(models.Model):
    entry_time = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
	
class ExitCount(models.Model):
	exit_time = models.DateTimeField(auto_now_add=True)
	location = models.ForeignKey(Location)
	
class TraficTimes(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	entry_count = models.IntegerField()
	exit_count = models.IntegerField()
	location = models.ForeignKey(Location)

class RushHour(models.Model):
	location = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	rush_hour = models.BooleanField(default=False) 
