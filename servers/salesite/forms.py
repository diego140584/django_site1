from django import forms



class LoginForm(forms.Form):

    login = forms.CharField(label="login", help_text="Введите свое имя")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль")
