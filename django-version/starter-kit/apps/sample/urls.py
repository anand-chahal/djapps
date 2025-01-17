from django.urls import path
from .views import SampleView, StudentsView, ChartData


urlpatterns = [
    path(
        "",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "charts/",
        SampleView.as_view(template_name="custom-chart.html"),
        name="charts",
    ),
    path(
        "charts/data",
        ChartData.as_view(),
        name="charts-data",
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
