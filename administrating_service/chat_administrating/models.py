from django.db import models
from django.utils.timezone import now


class ConversationThrough(models.Model):
    user = models.ForeignKey(
        to='auth_administrating.ChatUser',
        on_delete=models.CASCADE,
        null=True
    )
    conversation = models.ForeignKey(
        to='ConversationModel',
        on_delete=models.CASCADE
    )
    user_power = models.IntegerField(default=0)

    class Meta:
        db_table = 'users2conversations'
        verbose_name = 'Participant'


class ConversationModel(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(
        to='auth_administrating.ChatUser',
        related_name='+',
        through='ConversationThrough',
        through_fields=('conversation', 'user')
    )
    conversation_name = models.TextField(default='', blank=True)
    host = models.ForeignKey(to='auth_administrating.ChatUser', on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField(default=now, null=True)

    class Meta:
        db_table = 'conversations'

# Create your models here.
