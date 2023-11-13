from .models import Drive
from django.forms import ModelForm, TextInput, Textarea


class DriveForm(ModelForm):
    class Meta:
        model = Drive
        fields = ["name", "task", "phone", "email", "auto"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }), "task": Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите комментарий'
                }), "phone": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите номер телефона'
                    }), "email": TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Введите электронную почту'
                        }), "auto": TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Введите название машины'})}
