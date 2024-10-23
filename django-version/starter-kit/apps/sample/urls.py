from django.urls import path
from .views import SampleView, StudentsView


urlpatterns = [
    path(
        "",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "charts/",
        SampleView.as_view(template_name="charts.html"),
        name="charts",
    ),
    path(
        "maps/",
        SampleView.as_view(template_name="maps.html"),
        name="maps",
    ),
    path(
        "students/",
        StudentsView.as_view(template_name="students.html"),
        name="students",
    ),
]
