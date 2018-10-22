from django import forms



class LoginForm(forms.Form):

    login = forms.CharField(label="login", help_text="Введите свое имя", required=True)
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль", required=True, min_length=6)
