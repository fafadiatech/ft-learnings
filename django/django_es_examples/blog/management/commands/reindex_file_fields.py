# This management command has been written because django-elasticsearch
# app provides all facilities except for indexing FileField

from blog.models import Blog
from django.core.management.base import BaseCommand
from django_elasticsearch.client import es_client

class Command(BaseCommand):
    help = 'This command is used to re-index models including FileFields'

    def handle(self, *args, **options):
        Blog.es.reindex_all()
        index_name = Blog.es.index
        current_doc_type = Blog.es.doc_type

        # Index all file fields
        for blog in Blog.objects.all():
            current = blog.es.get(id=blog.id)
            current['cover_image'] = blog.cover_image_path

            es_client.index(index=index_name,
                doc_type=current_doc_type,
                id=blog.id,
                body=current)

        print "Completed Indexing"