from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from salesite.models import Customer
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class LoginForm(forms.Form):
    login = forms.CharField(label="login", help_text="Введите свое имя", required=True)
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль", required=True, min_length=6)
    required_css_class = "input[type=text]"
    required_css_class = "input[type=password]"


class RForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'login', 'gender', 'birth', 'firm',
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

    def save(self):

        try:
            if Customer.objects.get(name__exact=self.cleaned_data['name']) == self.cleaned_data['name'] or \
            Customer.objects.get(email__exact=self.cleaned_data['email']) == self.cleaned_data['email']:
                pass

        except:
            raise ValidationError("Customer couldnt be created!")

        else:
            obj = Customer.objects.create(
                name=self.cleaned_data['name'],
                last_name=self.cleaned_data['last_name'],
                login=self.cleaned_data['login'],
                gender=self.cleaned_data['gender'],
                birth=self.cleaned_data['birth'],
                firm=self.cleaned_data['firm'],
                phone=self.cleaned_data['phone'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],

            )
            return obj


