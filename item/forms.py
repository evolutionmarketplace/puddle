from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item name...'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Describe your item in detail...',
                'rows': 6
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'accept': 'image/*'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item name...'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Describe your item in detail...',
                'rows': 6
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'accept': 'image/*'
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-primary-600 focus:ring-primary-500'
            })
        }