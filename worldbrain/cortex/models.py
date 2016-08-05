from django.db import models
from django_fsm import FSMField, transition
from django_fsm_log.models import StateLog
from enum import Enum

class SourceStates(Enum):
    PENDING = 'pending'
    CRAWLED = 'crawled'
    REJECTED = 'rejected'
    FAILED = 'failed'

class AllUrlStates(Enum):
    PENDING = 'pending'
    PROCESSED = 'processed'


class Source(models.Model):
    domain_name = models.URLField()
    state = FSMField(default=SourceStates.PENDING.value, db_index=True)

    @transition(
        field=state,
        source='*',
        target=SourceStates.CRAWLED.value
    )
    def crawl(self):
        pass

    @transition(
        field=state,
        source='*',
        target=SourceStates.REJECTED.value
    )
    def reject(self):
        pass

    @transition(
        field=state,
        source=(SourceStates.CRAWLED.value),
        target=SourceStates.FAILED.value,
        custom=dict(admin=False)
    )
    def fail(self):
        pass

    @property
    def latest_crawl(self):
        try:
            return (
                self.transitions
                .filter(state=SourceStates.CRAWLED.value)
                .latest()
                .timestamp
            )
        except StateLog.DoesNotExist:
            return None

    def __str__(self):
            return 'Source [domain_name: {}] [state: {}]'.format(
                self.domain_name, self.state
            )


class AllUrl(models.Model):
    source = models.ForeignKey(
        Source,
        related_name='urls',
        related_query_name='url',
        on_delete=models.CASCADE
    )
    url = models.URLField()
    state = FSMField(default=AllUrlStates.PENDING.value, db_index=True)
    is_article = models.BooleanField(default=True)

    @transition(
        field=state,
        source='*',
        target=AllUrlStates.PROCESSED.value
    )
    def processed(self):
        pass

