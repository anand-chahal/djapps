from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""


class SampleView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


@method_decorator(login_required, name="dispatch")
class StudentsView(TemplateView):
    # sending custom context to the html page
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # add students
        context["names"] = ["Ishaan", "Vihaan", "Rajveer", "Saurya"]

        return context
