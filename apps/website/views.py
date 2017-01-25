from django.views.generic import FormView
from factory.forms import FactoryForm


class HomeView(FormView):
    template_name = "home.jinja2"
    form_class = FactoryForm
