from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import detail_route
import django_filters

from . import forms
from . import serializers
from .mixins import DefaultsMixin
from .models import Source, AllUrl

class SourceViewSet(DefaultsMixin, viewsets.ModelViewSet):

    model = Source
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer
    filter_class = forms.SourceViewFilter

    @detail_route()
    def urls(self, request, pk=None):
        source = self.get_object()
        serializer = serializers.AllUrlSerializer(source.urls.all(), context={'request': request}, many=True)
        return Response(serializer.data)

class AllUrlViewSet(DefaultsMixin, viewsets.ModelViewSet):

    model = AllUrl
    queryset = AllUrl.objects.all()
    serializer_class = serializers.AllUrlSerializer
    filter_class = forms.AllUrlViewFilter
