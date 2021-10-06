from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from blog.models import Post,UserData

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    login = forms.CharField(required=True,label="Login",widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(required=True,label="Parol",widget=forms.PasswordInput(attrs={"class":"form-class"}))
    password2 = forms.CharField(required=True,label="Parolni takrorlang",widget=forms.PasswordInput(attrs={"class":"form-class"}))
    phone = forms.CharField(required=True,label="Telefon",widget=forms.TextInput(attrs={"class":"form-class"}))
    adress = forms.CharField(required=True,label="adress",widget=forms.TextInput(attrs={"class":"form-class"}))

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(username=login).exists():
            raise ValidationError("bu login band")
        return login

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
            return password1
    def clean(self):
        super().clean()
        p1 = self.cleaned_data["password1"]
        p2 = self.cleaned_data["password2"]
        if p1 and p2 and p1 != p2:
            raise ValidationError("Paral mos emas")

    def save(self, commit=True):
        user = super().save(commit=False)
        login = self.cleaned_data['login']
        password1 = self.cleaned_data['password1']
        u = User.objects.create_user(username=login,password=password1)
        user.user = u
        if commit:
            user.save()
        return user
    class Meta:
        model = UserData
        fields = ('login','password1','password2','phone')
