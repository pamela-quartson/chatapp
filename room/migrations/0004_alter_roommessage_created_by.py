# Generated by Django 4.1.7 on 2023-02-17 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0003_alter_roommessage_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommessage',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
