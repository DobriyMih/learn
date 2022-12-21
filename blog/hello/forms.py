from django import forms



class UserForm(forms.Form):
    email = forms.CharField(help_text="Веддіть свій опобліковий запис")
    name = forms.CharField(help_text="Веддіть ім'я та прізвище")
    phone = forms.IntegerField(help_text="Веддіть свій номер телефону")

