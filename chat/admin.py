from django.contrib import admin
from .models import ChatGroup
# Register your models here.

class ChatGroupAdmin(admin.ModelAdmin):

    list_display = ('id','name','description','icon','mute_notification','created_at','updated_at')
    list_filter = ('id', 'name', 'description', 'icon', 'mute_notification', 'created_at', 'updated_at')
    list_display_links = ('name',)

admin.site.register(ChatGroup,ChatGroupAdmin)