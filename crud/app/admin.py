from django.contrib import admin # type: ignore

# Register your models here.

from .models import Operations
admin.site.register(Operations)