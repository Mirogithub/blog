from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Password confirmation')

    class Meta:
        model = User
        fields = ('email', 'first_name',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
