from django.core.management.base import BaseCommand

from worldbrain.cortex.models import AllUrl, Source

from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
url_list = list()


class DomainSpider(Spider):
    name = 'domainspider'

    def __init__(self, domain):
        self.source = domain
        self.start_urls = [domain.domain_name]

    def parse(self, response):

        global url_list

        try:

            body = response.body
            selector = Selector(text=body)
            for url in selector.css('a').xpath('@href').extract():
                url_list.append((url, self.source))

        except:
            pass  # TODO handle exception


def add_domain(domain):
    global process
    process.crawl(DomainSpider, domain=domain)


class Command(BaseCommand):
    help = 'Makes a list of all URLs for a given domain'

    def handle(self, *args, **options):

        global process

        domain_list = Source.objects.all().filter(processed_spider=False)

        for domain in domain_list:
            add_domain(domain)

        process.start()

        for url, source in url_list:

            new_url = AllUrl(source=source, url=url, is_article=False)
            try:
                new_url.save()
            except:
                pass  # TODO handle exception
