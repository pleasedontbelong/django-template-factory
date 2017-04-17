# from unittest import TestCase
from django.test import TestCase
from factory.forms import FactoryForm
from factory.constants import ADDONS

from mock import patch, ANY


class GeneratorTestCase(TestCase):

    @patch('factory.forms.Generator')
    def test_jinja2_pipeline(self, generator_mock):
        """
        When selecting jinja2 and pipeline, the jinja2_pipeline should be selected
        """
        data = {
            'name': "test",
            'jinja2': True,
            'pipeline': True,
        }
        form = FactoryForm(data=data)
        self.failUnless(form.is_valid())
        form.generate()
        expected_config = {
            'addons': [
                ADDONS.PIPELINE.choice_entry,
                ADDONS.JINJA2_PIPELINE.choice_entry
            ]
        }
        generator_mock.assert_called_with(expected_config, quiet=ANY, dry_run=ANY)
