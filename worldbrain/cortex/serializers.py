from rest_framework import serializers

from .models import Source, AllUrl


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    all_urls = serializers.HyperlinkedIdentityField(
        view_name='api:source-urls')
    processed_linkchecker = serializers.NullBooleanField(write_only=True,
                                                         required=False)

    class Meta:
        model = Source
        fields = ('domain_name', 'state', 'trusted_source', 'all_urls',
                  'processed_linkchecker')
        read_only_fields = ('state', 'all_urls',)

    def create(self, validated_data):
        validated_data.pop('processed_linkchecker', None)
        return Source.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.domain_name = validated_data.get('domain_name',
                                                  instance.domain_name)
        if validated_data.get('processed_linkchecker'):
            instance.crawl()

        instance.save()
        return instance


class AllUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllUrl
        fields = ('id', 'source', 'url', 'state', 'is_article')
        read_only_fields = ('state',)
