from django.contrib import admin

# Register your models here.
from django.contrib import admin
from photo.models import Photo

admin.site.register(Photo)
