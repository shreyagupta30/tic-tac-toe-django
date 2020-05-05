# Generated by Django 3.0.5 on 2020-04-21 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitation_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True, help_text="It's always nice to add a friendly message!", max_length=300, verbose_name='Optional Message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text='Please select the user you want to play a game with.', on_delete=django.db.models.deletion.CASCADE, related_name='invitation_received', to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]
