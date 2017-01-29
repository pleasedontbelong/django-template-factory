from django.views.generic import FormView
from factory.forms import FactoryForm


class HomeView(FormView):
    template_name = "home.jinja2"
    form_class = FactoryForm

    def form_valid(self, form):
        form.generate()
        return super(HomeView, self).form_valid(form)
