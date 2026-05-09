from django import forms
from core.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'image', 'name', 'description', 'rooms',
            'floor', 'location', 'available_numbers', 'price', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Loyiha nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Loyiha haqida',
                'rows': 4
            }),
            'rooms': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Xonalar soni'
            }),
            'floor': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Qavatlar soni'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Manzil'
            }),
            'available_numbers': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': "Bo'sh xonalar"
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Narx (USD)'
            }),
            'status': forms.Select(attrs={
                'class': 'form-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-file-input',
                'accept': 'image/*'
            }),
        }
        labels = {
            'image': 'Rasm',
            'name': 'Nomi',
            'description': 'Tavsif',
            'rooms': 'Xonalar soni',
            'floor': 'Qavatlar soni',
            'location': 'Joylashuv',
            'available_numbers': "Bo'sh xonalar",
            'price': 'Narx ($)',
            'status': 'Holati',
        }
