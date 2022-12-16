from django.contrib import admin
from .models import Messages
# Register your models here.
class Msreg(admin.ModelAdmin):
    list = ('message')
    admin.site.register(Messages)