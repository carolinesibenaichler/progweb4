from django import forms

class FormEntrar(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=8)
