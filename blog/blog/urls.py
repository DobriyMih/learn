from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path("index/", TemplateView.as_view(template_name="index.html")),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
]