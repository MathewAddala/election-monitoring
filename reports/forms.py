from django import forms
from .models import IssueReport

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


class IssueReportForm(forms.ModelForm):
    class Meta:
        model  = IssueReport
        fields = ['election', 'title', 'description', 'severity', 'evidence']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title':       'Brief title of the issue',
            'description': 'Describe the issue in detail…',
        }
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = FILE_CSS
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = SELECT_CSS
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = TEXTAREA_CSS
            else:
                field.widget.attrs['class'] = INPUT_CSS
            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]