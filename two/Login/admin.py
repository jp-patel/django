from django.contrib import admin
from .models import Member

class Memberadmin(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(Member,Memberadmin)

# Register your models here.
