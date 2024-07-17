from django.forms import (
    ModelForm, Textarea, EmailInput, TextInput
)

from .models import Massage


class SendMessageForm(ModelForm):
    
    class Meta:
        
        model = Massage
        fields = '__all__'        
        widgets = {
            'name' : TextInput(attrs={'class':"input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold px-4" , 'placeholder':'نام'}),
            'email' : EmailInput(attrs={'class':"input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold px-4" , 'placeholder':'ایمیل'}),
            'message': Textarea(attrs={'class':"input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold px-4", 'placeholder':'متن...'}),
        }
        labels = {
            'name' : '',
            'email' : '',
            'message' : '',
        }
        