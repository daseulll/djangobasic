from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  #모든 필드가 다 불러와져 자동 저장