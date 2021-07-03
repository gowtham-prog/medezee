from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(gender)
admin.site.register(hospital)
admin.site.register(department)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(Location)
admin.site.register(medicine)
admin.site.register(test)