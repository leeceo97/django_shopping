from django import forms
from .models import Order

class RegisterForm(forms.Form):
    product = forms.IntegerField(
        error_messages={
            'required': '상품명을입력하세요.'
        }, label='상품', widget=forms.HiddenInput
    )
    quantity = forms.IntegerField(
        error_messages ={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    
    def clean(self):
        cleaned_data= super().clean()
        