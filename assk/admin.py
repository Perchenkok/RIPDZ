from django.contrib import admin
from assk import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Post)
admin.site.register(models.Answer)
admin.site.register(models.Tags)