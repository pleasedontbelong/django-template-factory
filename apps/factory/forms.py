from django import forms
from .constants import FIELDS_MAP


class FactoryForm(forms.Form):
    pipeline = forms.BooleanField(label="Add Pipeline", required=False)
    jinja2 = forms.BooleanField(label="Add Jinja2", required=False)
    extended_choices = forms.BooleanField(label="Add Extended Choices", required=False)
    braces = forms.BooleanField(label="Add Django Braces", required=False)

    def generate(self):
        settings = {
            'addons': [FIELDS_MAP[k] for k, v in self.cleaned_data.iteritems() if v]
        }
        print settings
