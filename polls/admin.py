from django.contrib import admin
from .models import Food, Poll

# Register your models here.


admin.site.register(Poll)
admin.site.register(Food)