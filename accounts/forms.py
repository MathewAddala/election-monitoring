from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Shared CSS classes for form widgets
INPUT_CSS = (
    'w-full px-4 py-3 bg-slate-900/80 border border-slate-600 rounded-xl '
    'text-white placeholder-slate-500 focus:outline-none focus:ring-2 '
    'focus:ring-blue-500 focus:border-transparent transition-all duration-200'
)
SELECT_CSS = (
    'w-full px-4 py-3 bg-slate-900/80 border border-slate-600 rounded-xl '
    'text-white focus:outline-none focus:ring-2 focus:ring-blue-500 '
    'focus:border-transparent transition-all duration-200 appearance-none'
)
TEXTAREA_CSS = (
    'w-full px-4 py-3 bg-slate-900/80 border border-slate-600 rounded-xl '
    'text-white placeholder-slate-500 focus:outline-none focus:ring-2 '
    'focus:ring-blue-500 focus:border-transparent transition-all duration-200 resize-y'
)
FILE_CSS = (
    'w-full text-sm text-slate-400 file:mr-4 file:py-2.5 file:px-4 '
    'file:rounded-xl file:border-0 file:text-sm file:font-semibold '
    'file:bg-blue-600 file:text-white hover:file:bg-blue-500 '
    'file:cursor-pointer file:transition-all cursor-pointer'
)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username':  'Choose a username',
            'email':     'you@example.com',
            'phone':     '+91 XXXXX XXXXX',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }
        for name, field in self.fields.items():
            field.widget.attrs['class'] = INPUT_CSS
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]


class ProfileForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name':  'Last name',
            'email':      'you@example.com',
            'phone':      '+91 XXXXX XXXXX',
        }
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = FILE_CSS
            else:
                field.widget.attrs['class'] = INPUT_CSS
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]