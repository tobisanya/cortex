import django_filters

from .models import Source, AllUrl


class SourceViewFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ['state']


class AllUrlViewFilter(django_filters.FilterSet):
    class Meta:
        model = AllUrl
        fields = ['state', 'is_article']
