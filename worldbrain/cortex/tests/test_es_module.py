import pytest
import time

from django.core.management import call_command
from worldbrain.cortex.search.indexes import ArticleIndex


@pytest.mark.django_db
@pytest.mark.usefixtures('article_fixture')
def test_index_article():
    call_command('index')
    time.sleep(5)
    search = ArticleIndex()
    search.PHRASE = 'very_unique_title'
    search.SIZE = 1
    search.OFFSET = 0
    search.FILTERS = {'domain_name': 'domain_name'}
    es_data = search.find()
    assert es_data['hits']['total'] >= 1
