from django.contrib import admin

# Register your models here.
from .models import Torrent, 


@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin):
    pass

@admin.register(Trend)
class TrebdAdmin(admin.ModelAdmin):
    pass

