from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError




class LoginForm(forms.Form):

    login = forms.CharField(label="login", help_text="Введите свое имя", required=True)
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль", required=True, min_length=6)
    required_css_class = "input[type=text]"
    required_css_class = "input[type=password]"


class RegForm(forms.Form):

    name = forms.CharField(label="name", required=True)
    last_name = forms.CharField(label="last name", required=True)
    gender = forms.CharField(label="gender", required=True)
    birth = forms.DateField(label="birth date", widget=AdminDateWidget, required=True)
    firm = forms.CharField(label="firm", required=True)
    phone = forms.CharField(label="phone", required=True)
    email = forms.EmailField(label="email", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="password", help_text="не меньше 8 символов", required=True, min_length=8)
    re_password = forms.CharField(widget=forms.PasswordInput, label="re password", help_text="Повторите ввод пароля", required = True, min_length=8)
    name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    gender.widget.attrs.update({'class': 'form-control'})
    firm.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    re_password.widget.attrs.update({'class': 'form-control'})