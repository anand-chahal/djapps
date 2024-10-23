from django.urls import path
from .views import SampleView


urlpatterns = [
    path(
        "",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "ishu/",
        SampleView.as_view(template_name="ishu.html"),
        name="ishu",
    ),
    path(
        "adi/",
        SampleView.as_view(template_name="adi.html"),
        name="adi",
    ),
]
