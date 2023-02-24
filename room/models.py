from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class RoomMessage(models.Model):
    text = models.CharField(max_length=255)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at', )
