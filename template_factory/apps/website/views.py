from django.views.generic import FormView
from django.template.response import TemplateResponse
from factory.forms import FactoryForm


class HomeView(FormView):
    template_name = "home.jinja2"
    form_class = FactoryForm
    success_url = 'home'

    def form_valid(self, form):
        generator = form.generate()
        context = {
            'log': generator._log,
            'branch': generator.build_branch,
            'name': form.cleaned_data['name']
        }
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=context
        )
