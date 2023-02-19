from django.contrib import admin
from .models import ChatUser
from .forms import ChatUserForm


@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'login']
    form = ChatUserForm


# Register your models here.
