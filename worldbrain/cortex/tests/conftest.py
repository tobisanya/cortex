import pytest


@pytest.fixture()
def article_fixture():
    from worldbrain.cortex.models import Article

    article_dict = {
        'url': 'url',
        'domain_name': 'domain_name',
        'title': 'very_unique_title',
        'html': 'html',
        'publish_date': '2016-07-25',
        'parse_time': 'parse_time',
        'state': 'parsed',
    }
    Article.objects.create(**article_dict)
