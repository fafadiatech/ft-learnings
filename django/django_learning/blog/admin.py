# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog
from reversion.admin import VersionAdmin

@admin.register(Blog)
class BlogAdmin(VersionAdmin):
    pass
