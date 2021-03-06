from django import forms
from rbac.models import User
from django.core.exceptions import ValidationError
from rbac.forms.base import BaseForm


class UserModelForm(BaseForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password


class UpdateUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class ResetUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = User
        fields = ['password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password
