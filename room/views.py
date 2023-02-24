from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Room, RoomMessage
from .forms import NewMessageForm


@login_required
def rooms(request):
    rooms = Room.objects.all()
    query = request.GET.get('query', '')
    if query:
        rooms = Room.objects.filter(Q(name__icontains=query))

    context = {'rooms': rooms, 'query': query}
    return render(request, 'room/index.html', context)


@login_required
def detail(request, slug):
    room = Room.objects.get(slug=slug)
    messages = RoomMessage.objects.filter(room=room)
    form = NewMessageForm()

    context = {'room': room, 'form': form, 'messages': messages}

    return render(request, 'room/detail.html', context)
