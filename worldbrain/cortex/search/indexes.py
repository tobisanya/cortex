from elasticsearch import Elasticsearch
from django.conf import settings


class ArticleIndex(object):
    ES_HOST = settings.ES['host']
    ES_INDEX = settings.ES['index']
    ES_ARTICLE_TYPE = settings.ES['article_type']

    def __init__(self):
        self.es = Elasticsearch([self.ES_HOST])

    def reindex(self, body, id=''):
        if id:
            self.es.index(index=self.ES_INDEX,
                          doc_type=self.ES_ARTICLE_TYPE,
                          body=body,
                          id=id)
        else:
            self.es.index(index=self.ES_INDEX,
                          doc_type=self.ES_ARTICLE_TYPE,
                          body=body)

    def find(self, search_phrase):
        if search_phrase:
            body = {
                "query": {
                    "bool": {
                        "should": [
                            {
                                "match": {
                                    "title": {
                                        "query": search_phrase,
                                        "boost": 2
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        else:
            body = {"query": {"match_all": {}}}
        return self.es.search(index=self.ES_INDEX, doc_type=self.ES_ARTICLE_TYPE, body=body)
