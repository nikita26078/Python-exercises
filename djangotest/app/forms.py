from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateInput, Select, FileInput, Textarea, CharField, PasswordInput, Form

from .models import News, Feedback


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'desc', 'body', 'date', 'user', 'category', 'image']

        labels = {
            'title': 'Заголовок',
            'body': 'Текст',
            'desc': 'Описание',
            'date': 'Дата',
            'user': 'Пользователь',
            'category': 'Категория',
            'image': 'Изображение'
        }
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание статьи',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "user": Select(attrs={
                'class': 'form-control',
            }),
            "category": Select(attrs={
                'class': 'form-control',
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
            }),
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['text']
        labels = {
            'text': "Отзыв"
        }

        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            }),
        }


class UserRegistrationForm(ModelForm):
    password = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Повторите пароль', widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Пароли не совпадают.')
        return cd['password2']


class LoginForm(Form):
    username = CharField(label='Имя пользователя')
    password = CharField(label='Пароль', widget=PasswordInput)
