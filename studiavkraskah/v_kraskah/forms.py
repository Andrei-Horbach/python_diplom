from .models import UserCallBack
from django.forms import ModelForm, TextInput


# Форма для обратного звонка
class Course_registration(ModelForm):
    class Meta:
        model = UserCallBack
        fields = ['name', 'phoneNumber']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'phoneNumber': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
        }