from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AdvertisemenForm(forms.ModelForm):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))

    price = forms.DecimalField( max_digits=10, widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))

    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))



class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'surname')
