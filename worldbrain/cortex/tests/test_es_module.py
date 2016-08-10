import pytest

from django.core.management import call_command
from worldbrain.cortex.search.indexes import ArticleIndex


@pytest.mark.django_db
@pytest.mark.usefixtures('article_fixture')
def test_index_article():
    if call_command('reindex'):
        search = ArticleIndex()
        es_data = search.find('very_unique_title')
        assert es_data['hits']['total'] == 1
