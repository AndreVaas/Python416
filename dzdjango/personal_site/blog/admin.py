from django.contrib import admin
from .models import Blog

admin.site.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
