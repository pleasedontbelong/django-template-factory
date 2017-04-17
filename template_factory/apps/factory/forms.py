from django import forms
from django.conf import settings
from .fabfile import Generator
from .constants import FIELDS_MAP


class FactoryForm(forms.Form):
    name = forms.CharField(label="Project Name", required=True)
    pipeline = forms.BooleanField(label="Add Pipeline", required=False)
    jinja2 = forms.BooleanField(label="Add Jinja2", required=False)
    extended_choices = forms.BooleanField(label="Add Extended Choices", required=False)
    braces = forms.BooleanField(label="Add Django Braces", required=False)
    rest_framework = forms.BooleanField(label="Add Django Rest Framework", required=False)

    def generate(self):
        # If jinja2 and pipeline are selected, use a different jinja2 branch
        if self.cleaned_data['jinja2'] and self.cleaned_data['pipeline']:
            del self.cleaned_data['jinja2']
            self.cleaned_data['jinja2_pipeline'] = True
        config = {
            'addons': [FIELDS_MAP[k].choice_entry for k, v in self.cleaned_data.iteritems() if v and k != "name"]
        }
        generator = Generator(config, dry_run=settings.GENERATOR_DRY_RUN, quiet=True)
        generator.run()
        return generator
