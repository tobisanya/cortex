from rest_framework import serializers
from django_fsm import can_proceed

from .models import SourceStates, Source, AllUrl

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    all_urls = serializers.HyperlinkedIdentityField(view_name='source-urls')
    processed_linkchecker = serializers.NullBooleanField(write_only=True)

    class Meta:
        model = Source
        fields = ('domain_name', 'state', 'all_urls', 'processed_linkchecker')
        read_only_fields = ('state', 'all_urls', )
        
    def update(self, instance, validated_data):
        if not can_proceed(instance.crawl):
            raise PermissionDenied

        instance.domain_name = validated_data.get('domain_name', instance.domain_name)
        if validated_data.get('processed_linkchecker'):
            instance.crawl()
        else:
            if instance.state == SourceStates.CRAWLED.value:
                instance.fail()
            else:
                instance.reject()

        instance.save()
        return instance

class AllUrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = AllUrl
        fields = ('id', 'source', 'url', 'state', 'is_article')
        read_only_fields = ('state', )