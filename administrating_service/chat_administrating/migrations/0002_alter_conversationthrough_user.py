# Generated by Django 4.1.7 on 2023-02-21 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_administrating', '0002_alter_chatuser_id'),
        ('chat_administrating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationthrough',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_administrating.chatuser'),
        ),
    ]
