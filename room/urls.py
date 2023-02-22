from django.urls import path

from . import views

app_name = 'room'

urlpatterns = [
    path('', view=views.rooms, name='rooms'),
    path('<slug:slug>/', view=views.detail, name='detail'),
]
