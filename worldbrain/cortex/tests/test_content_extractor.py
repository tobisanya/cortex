import pytest

from worldbrain.cortex.content_extractor import ContentExtractor
from worldbrain.cortex.models import Article


@pytest.mark.django_db
@pytest.mark.usefixtures('url_fixture')
def test_extract_content():
    content_extractor = ContentExtractor()
    content_extractor.extract_content()
    assert Article.objects.count() == 1
