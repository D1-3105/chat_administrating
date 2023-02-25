# Generated by Django 4.1.7 on 2023-02-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_administrating', '0003_conversationmodel_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversationthrough',
            options={'verbose_name': 'Participant'},
        ),
        migrations.AddField(
            model_name='conversationmodel',
            name='conversation_name',
            field=models.TextField(blank=True, default=''),
        ),
    ]
