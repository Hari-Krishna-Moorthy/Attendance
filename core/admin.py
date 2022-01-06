from django.contrib import admin

# Register your models here.

from core.models import Profile, Attendance

admin.site.register(Profile)
admin.site.register(Attendance)
