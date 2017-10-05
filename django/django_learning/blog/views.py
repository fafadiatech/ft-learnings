# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Blog

class IndexTableView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexTableView, self).get_context_data(**kwargs)
        context['entries'] = Blog.objects.all()
        return context
