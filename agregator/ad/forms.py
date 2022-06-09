from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255,label='Название объявления')
    #photo = forms.ImageField(label='Фотографии')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',empty_label='Категория не вбырана')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Описание объявления')
    cost = forms.IntegerField(label='Цена')
    phone = forms.IntegerField(label='Контактный телефон')
    mail = forms.CharField(max_length=255,label='Электронная почта')
    is_published = forms.BooleanField(label='Публикация',required=False,initial=True)
