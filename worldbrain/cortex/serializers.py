from rest_framework import serializers

from .models import Source, AllUrl

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    all_urls = serializers.HyperlinkedIdentityField(view_name='source-urls')

    class Meta:
        model = Source
        fields = ('domain_name', 'state', 'all_urls', 'latest_crawl')
        read_only_fields = ('state', 'latest_crawl', 'all_urls', )

class AllUrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = AllUrl
        fields = ('id', 'source', 'url', 'state', 'is_article')
        read_only_fields = ('state', )