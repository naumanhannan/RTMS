from rest_framework import serializers
from music.models import  VehicleCount
from music.models import  ExitCount
from music.models import TraficTimes


class VehicleCountserializer(serializers.ModelSerializer):
	class Meta:
		model = VehicleCount
		fields = [
		'entry_time',
		'location',
		]


class ExitCountserializer(serializers.ModelSerializer):
	class Meta:
		model = ExitCount
		fields = [
		'exit_time',
		'location',
		]

class TraficTimesSerializer(serializers.ModelSerializer):
	class Meta:
		model = TraficTimes
		fields = [
		'start_time',
		'end_time',
		'location',
		'entry_count',
		'exit_count'
		]