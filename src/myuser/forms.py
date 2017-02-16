from django.contrib.auth.forms import UserCreationForm
from django import forms
from myuser.models.myuser import User

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password')

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
