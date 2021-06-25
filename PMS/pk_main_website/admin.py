from django.contrib import admin

# Register your models here.

# Rigester Board Models
from .models import *


admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Task)
