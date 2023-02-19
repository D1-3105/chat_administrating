from django import forms
from .models import ChatUser


class ChatUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ChatUser
        exclude = 'id',
