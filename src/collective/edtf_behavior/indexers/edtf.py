# -*- coding: utf-8 -*-
from collective.edtf_behavior.behaviors.edtf_date import IEDTFDateMarker
from collective.edtf_behavior.behaviors.edtf_date import IEDTFDate
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """Dummy to prevent indexing child objects"""
    raise AttributeError('This field should not indexed here!')


@indexer(IEDTFDateMarker)
def edtf_date(obj):
    print(obj.edtf_date)
    return obj.edtf_date


@indexer(IDexterityContent)
def date_earliest(obj):
    print(obj.date_earliest)
    return obj.date_earliest


@indexer(IEDTFDate)
def date_latest(obj):
    print(obj.date_latest)
    return obj.date_latest


@indexer(IEDTFDateMarker)
def date_sort_ascending(obj):
    return obj.date_sort_ascending


@indexer(IEDTFDateMarker)
def date_sort_descending(obj):
    return obj.date_sort_descending
