from django.db import models
from django.contrib.auth.models import Group
from django.urls import  reverse
# Create your models here.

class ChatGroup(Group):
    description = models.TextField(blank=True, help_text="description of the group")
    mute_notification = models.BooleanField(default=False, help_text="disable notification if true")
    icon = models.ImageField(help_text="Group Icon", blank=True, upload_to="chartgroup")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('chat:room',args=[str(self.id)])