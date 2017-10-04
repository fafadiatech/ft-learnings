# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_elasticsearch.models import EsIndexable

class Blog(EsIndexable, models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    cover_image = models.FileField(upload_to="blog_cover_images", blank=True, null=True, default=None)

    @property
    def cover_image_path(self):
        return str(self.cover_image)

    def __unicode__(self):
        return self.title
