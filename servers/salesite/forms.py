from django import forms



class LoginForm(forms.Form):

    login = forms.CharField(label="login", help_text="Введите свое имя", required=True)
    password = forms.CharField(widget=forms.PasswordInput, help_text="Введите свое пароль", required=True, min_length=6)
    required_css_class = "input[type=text]"
    required_css_class = "input[type=password]"


class RegForm(forms.Form):

    name = forms.CharField(label="name", help_text="Введите свое имя", required=True)
    last_name = forms.CharField(label="last name", help_text="Введите свою фамилию", required=True)
    gender = forms.CharField(label="gender", help_text="Введите свое пол", required=True)
    birth = forms.DateField(label="birth", help_text="Выберите свою дату рождения", required=True)
    firm = forms.CharField(label="firm", help_text="Введите название своей компании", required=True)
    phone = forms.CharField(label="phone", help_text="Введите свое имя", required=True)
    email = forms.EmailField(label="email", help_text="Введите свое имя", required=True)
    password = forms.CharField(label="password", help_text="Введите свой пароль", required=True, min_length=8)
    re_password = forms.CharField(label="re password", help_text="Повторите свой пароль", required=True, min_length=8)
