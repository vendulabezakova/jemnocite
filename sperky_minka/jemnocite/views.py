from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
import jemnocite.models as models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"