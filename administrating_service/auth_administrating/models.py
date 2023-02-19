from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import hashlib
import base64


class ChatUser(models.Model):

    id:int = models.AutoField(primary_key=True)
    email: str = models.EmailField(unique=True)
    password: str = models.TextField()
    login: str = models.TextField(null=True)
    is_active: bool = models.BooleanField(default=False)

    __original_password = None

    class Meta:
        db_table = 'users'
        constraints = [
            models.UniqueConstraint(
                name='%(app_label)s_%(class)s_login_email_uniq',
                fields=('login', 'email')
            )
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_password = self.password

    def __str__(self):
        return f'{self.email=}, {self.login=}'

    def make_password(self):
        raw_hashed = hashlib.sha256(self.password.encode())
        if self.__original_password != self.password:
            self.password = base64.b64encode(raw_hashed.digest()).decode()




@receiver(pre_save, sender=ChatUser)
def make_user_password(instance: ChatUser, update_fields=None, **kwargs):
    if instance.password:
        instance.make_password()


# Create your models here.
