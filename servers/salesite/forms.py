from django import forms


class LoginForm(forms.Form):
    name = forms.CharField()
    lastName = forms.CharField()
    login = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
