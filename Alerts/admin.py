from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Neighborhood)
admin.site.register(models.Location)
admin.site.register(models.Profile)
admin.site.register(models.Business)
admin.site.register(models.Postii)