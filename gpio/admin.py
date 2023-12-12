from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.GPIO)
admin.site.register(models.Button)
admin.site.register(models.SystemInfo)
