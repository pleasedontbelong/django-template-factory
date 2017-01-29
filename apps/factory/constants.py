from extended_choices import Choices


CORE_REPO = "git@github.com:pleasedontbelong/django-template.git"
ADDONS = Choices(
    ('JINJA2', 'addon/jinja2/2_8', 'Jinja2 Templates'),
    ('PIPELINE', 'addon/pipeline/1_6', 'Pipeline'),
    ('EXTENDED_CHOICES', 'addon/extended_choices/1_1', 'Pipeline'),

)

FIELDS_MAP = {
    "pipeline": ADDONS.PIPELINE,
    "jinja2": ADDONS.JINJA2,
    "extended_choices": ADDONS.EXTENDED_CHOICES,
}
