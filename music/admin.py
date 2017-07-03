from django.contrib import admin

from .models import TraficTimes
from .models import Location

from .models import VehicleCount
class VehicleCountAdmin(admin.ModelAdmin):
    list_display = ('entry_time','location')

from .models import ExitCount
class ExitCountAdmin(admin.ModelAdmin):
    list_display = ('exit_time','location')

class TraficTimesAdmin(admin.ModelAdmin):
	list_display=('start_time','end_time','entry_count' , 'exit_count' , 'location') 


admin.site.register(VehicleCount , VehicleCountAdmin)
admin.site.register(ExitCount , ExitCountAdmin)
admin.site.register(TraficTimes , TraficTimesAdmin)
admin.site.register(Location)


