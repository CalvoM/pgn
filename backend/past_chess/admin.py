from django.contrib import admin

from .models import Game

admin.site.register(Game)

admin.site.site_title = "Past Chess"
admin.site.site_header = "Past Chess Admin"
admin.site.index_title = "Admin"

# Register your models here.
