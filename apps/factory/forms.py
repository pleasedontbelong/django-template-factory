from django import forms


class FactoryForm(forms.Form):
    pipeline = forms.BooleanField(label="Add Pipeline")
    jinja2 = forms.BooleanField(label="Add Jinja2")
