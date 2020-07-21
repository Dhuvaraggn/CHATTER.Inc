from django.contrib import admin
from .models import Room,Member,Message,Accounts
# Register your models here.
admin.site.register(Room)
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Accounts)

