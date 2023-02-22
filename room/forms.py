from django import forms

from .models import RoomMessage


class NewMessageForm(forms.ModelForm):
    class Meta:
        model = RoomMessage
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border flex-1 mr-1', 
                'id': 'chat-message-input', 
                'name': 'text', 
                'placeholder': 'Your message here...'
            })
        }
        labels = {'text': ''}
