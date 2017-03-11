# Full configuration in http://niwinz.github.io/django-jinja/latest/#_installation
from django_jinja.builtins import DEFAULT_EXTENSIONS

INSTALLED_APPS += ('django_jinja',)  # NOQA

TEMPLATES += [  # NOQA
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja2",
            "app_dirname": "jinja2",
            "auto_reload": True,
            # "environment": "myproject.jinja2.environment",
            "extensions": DEFAULT_EXTENSIONS + ["pipeline.jinja2.PipelineExtension"],
            "filters": {
                "add_class": "base.filters.add_class",
            },
        }
    },
]
