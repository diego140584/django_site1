from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from  salesite.models import Customer
from django.core.exceptions import ValidationError




class LoginForm(forms.Form):

    login = forms.CharField(label="login", help_text="Введите свое имя", required=True)
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль", required=True, min_length=6)
    required_css_class = "input[type=text]"
    required_css_class = "input[type=password]"



class RForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'login', 'gender',  'birth', 'firm',
                  'phone', 'email', 'password', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'firm': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),


        }


