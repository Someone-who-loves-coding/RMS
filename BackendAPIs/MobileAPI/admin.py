from django.contrib import admin
from .models import Employeetable,PeripheralRequest

# Register the models with the admin site
admin.site.register(Employeetable)
admin.site.register(PeripheralRequest)