from django.contrib import admin
from .models import files,SuperUser

# Register your models here.
admin.site.register(files)
admin.site.register(SuperUser)
