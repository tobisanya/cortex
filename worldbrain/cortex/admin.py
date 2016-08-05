from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin

from .models import Source, AllUrl

@admin.register(Source)
class SourceAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ('state',)
    readonly_fields = ('state', 'latest_crawl')

@admin.register(AllUrl)
class SourceAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ('state',)
    readonly_fields = ('state', )
