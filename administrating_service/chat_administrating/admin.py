from django.contrib import admin
from .models import ConversationThrough, ConversationModel


@admin.register(ConversationThrough)
class ParticipantModel(admin.ModelAdmin):
    list_display = ['conversation_id', 'user_id', 'id']


@admin.register(ConversationModel)
class ConversationModel(admin.ModelAdmin):
    list_display = ['id', 'host_id']


# Register your models here.
