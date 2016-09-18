import pytest


@pytest.fixture()
def article_fixture():
    from worldbrain.cortex.models import Article

    article_dict = {
        'url': 'url',
        'domain_name': 'domain_name',
        'title': 'very_unique_title',
        'publish_date': '2016-07-25',
        'parse_time': 'parse_time',
        'state': 'parsed',
    }
    Article.objects.create(**article_dict)


@pytest.fixture()
def url_fixture():
    from worldbrain.cortex.models import AllUrl, Source
    source = Source(domain_name='www.collective-evolution.com', state='ready')
    source.save()

    url = 'http://www.collective-evolution.com/2016/09/07/'
    url2 = 'astronomers-just-found-a-second-dyson-sphere'
    url3 = '-star-alien-star-with-odd'
    url4 = '-variations-of-brightness/'
    url = url + url2 + url3 + url4

    from urllib import request
    test_html = str(request.urlopen(url).read())

    url_dict = {
        'source': source,
        'url': url,
        'state': 'pending',
        'is_article': 'True',
        'html': test_html
    }

    AllUrl.objects.create(**url_dict)
