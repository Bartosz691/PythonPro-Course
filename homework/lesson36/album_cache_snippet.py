from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets


@method_decorator(cache_page(60 * 5), name='list')
class AlbumViewSet(viewsets.ModelViewSet):
    """
    Lista albumów jest cachowana przez 5 minut.

    W projekcie właściwym klasa zawiera również queryset,
    serializer_class oraz permissions.
    """

    pass