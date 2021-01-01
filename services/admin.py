from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Type')

admin.site.register(Contact,ContactAdmin)
