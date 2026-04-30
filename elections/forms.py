from django import forms
from .models import Election, ElectionUpdate

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


class ElectionForm(forms.ModelForm):
    class Meta:
        model  = Election
        fields = ['title', 'description', 'election_date', 'location', 'status']
        widgets = {
            'election_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title':       'Election title',
            'description': 'Provide details about this election…',
            'location':    'City, State or Region',
        }
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = SELECT_CSS
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = TEXTAREA_CSS
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = INPUT_CSS
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]


class ElectionUpdateForm(forms.ModelForm):
    class Meta:
        model  = ElectionUpdate
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget = forms.Textarea(attrs={
            'class': TEXTAREA_CSS,
            'rows': 3,
            'placeholder': 'Write an update for this election…',
        })