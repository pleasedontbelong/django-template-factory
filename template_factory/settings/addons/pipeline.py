# full configuration https://django-pipeline.readthedocs.io/en/latest/configuration.html

INSTALLED_APPS += [
    'pipeline',
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# To enable with jinja2 add
# 'OPTIONS': {
#     'environment': 'myproject.jinja2.environment',
#     'extensions': ['pipeline.jinja2.PipelineExtension']
# }
# to the jinja2 env


PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'home': {
            'source_filenames': (
                'css/home.css',
            ),
            'output_filename': 'css/home.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
}
