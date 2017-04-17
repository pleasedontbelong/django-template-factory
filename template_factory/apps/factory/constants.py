from extended_choices import Choices


CORE_REPO = "git@github.com:pleasedontbelong/django-template.git"
ADDONS = Choices(
    ('JINJA2', 'addon/jinja2/2_8', 'Jinja2 Templates'),
    ('PIPELINE', 'addon/pipeline/1_6', 'Pipeline'),
    ('EXTENDED_CHOICES', 'addon/extended-choices/1_1', 'Extended Choices'),
    ('BRACES', 'addon/braces/1_11', 'Braces'),
    ('DRF', 'addon/restframework/3_2', 'Django Rest Framework'),
    ('JINJA2_PIPELINE', 'addon/jinja2_pipeline/2_8', 'Jinja2 for Pipeline Templates'),

)

FIELDS_MAP = {
    "pipeline": ADDONS.PIPELINE,
    "jinja2": ADDONS.JINJA2,
    "jinja2_pipeline": ADDONS.JINJA2_PIPELINE,
    "extended_choices": ADDONS.EXTENDED_CHOICES,
    "braces": ADDONS.BRACES,
    "rest_framework": ADDONS.DRF,
}
