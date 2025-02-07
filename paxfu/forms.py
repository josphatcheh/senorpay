
from django import forms
from .models import UserPaxfulPay

class UserForm(forms.ModelForm):
    class Meta:
        model = UserPaxfulPay
        fields = ['username', 'amount']