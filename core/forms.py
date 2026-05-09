from django import forms
from .models import Comments, Contact, Lead


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Ismingizni kiriting',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Izohingizni yozing',
                'required': True
            }),
        }

        labels = {
            'name': 'Ismingiz',
            'message': 'Izohingiz',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Ismingizni kiriting',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Email manzilingizni kiriting',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Xabaringizni yozing',
                'required': True
            }),
        }

        labels = {
            'name': 'Ismingiz',
            'email': 'Email manzilingiz',
            'message': 'Xabaringiz',
        }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone']

        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Ismingizni kiriting',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'id': 'phone',
                'class': 'form-control',
                'placeholder': 'Telefon raqamingizni kiriting',
                'required': True
            }),
        }

        labels = {
            'name': 'Ismingiz',
            'phone': 'Telefon',
        }