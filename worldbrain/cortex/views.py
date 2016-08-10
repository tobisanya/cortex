from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from worldbrain.cortex import forms
from worldbrain.cortex import serializers
from worldbrain.cortex.mixins import DefaultsMixin
from worldbrain.cortex.models import Source, AllUrl
from worldbrain.cortex.search.indexes import ArticleIndex


class SourceViewSet(DefaultsMixin, viewsets.ModelViewSet):
    model = Source
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer
    filter_class = forms.SourceViewFilter

    @detail_route()
    def urls(self, request, pk=None):
        source = self.get_object()
        serializer = serializers.AllUrlSerializer(source.urls.all(),
                                                  context={'request': request},
                                                  many=True)
        return Response(serializer.data)


class AllUrlViewSet(DefaultsMixin, viewsets.ModelViewSet):
    model = AllUrl
    queryset = AllUrl.objects.all()
    serializer_class = serializers.AllUrlSerializer
    filter_class = forms.AllUrlViewFilter


class SearchViewSet(viewsets.ViewSet):
    def list(self, request):
        search = ArticleIndex()
        if request.GET.get('q', None):
            es_data = search.find(request.GET.get('q'))
            return Response(es_data)
        else:
            es_data = search.find('')
            return Response(es_data)
