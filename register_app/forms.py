from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label="Username")
    password = forms.CharField(
        max_length=100,
        required=False,
        label="Password",
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(required=False, label="Email")
    contact_number = forms.CharField(max_length=20, required=False, label="Contact Number")
