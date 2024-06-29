from django import forms
from django.views.decorators.csrf import csrf_protect


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Name",
        'class': "contact__input",
        "color": "#e75480",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'class': "contact__input",
        "color": "#e75480",

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={

        'name': "Message",
        "cols": 0,
        "rows": 10,
        "class": "contact__input",
    }))
