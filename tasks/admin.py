from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Task)

admin.site.register(TaskCategoy)

admin.site.register(TaskAssignment)

admin.site.register(Member)
