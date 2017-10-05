# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField(max_length=255)
    blurb = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    tags = TaggableManager()

    def __unicode__(self):
        return self.tite

