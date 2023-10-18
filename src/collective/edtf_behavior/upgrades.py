# -*- coding: utf-8 -*-
from __future__ import absolute_import
from plone.app.upgrade.utils import loadMigrationProfile
from plone import api
import transaction
from .behaviors.edtf_date import IEDTFDate, IEDTFDateMarker
import edtf2
from edtf2.parser.edtf_exceptions import EDTFParseException
import logging

logger = logging.getLogger('collective.edtf_bahviour.upgrades')


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-collective.edtf_behavior:default',
    )


def to_1002(context):
    # for each existing edtf_date: check if its parsable; if not, try to convert it
    count_total = 0
    count_values = 0
    count_nochanges = 0
    count_parser_errors = 0
    count_other_errors = 0
    count_converts = 0

    # find all of our etdf values
    edtfs = api.content.find(object_provides=[IEDTFDateMarker, IEDTFDate])
    logger.info("Starting to check edtf_date values of {0} items".format(len(edtfs)))
    for brain in edtfs:
        obj = brain.getObject()
        adapted_obj = IEDTFDate(obj)
        count_total = count_total + 1
        if adapted_obj.edtf_date:
            value = adapted_obj.edtf_date
            count_values = count_values + 1
            try:
                # if its parsable nothing has to be done
                edtf2.parse_edtf(value)
                count_nochanges = count_nochanges + 1
            except EDTFParseException:
                # if there is ParseException, try to convert value to new specification and try to parse again
                new_expression = edtf2.old_specs_to_new_specs_expression(value)
                try:
                    edtf2.parse_edtf(new_expression)
                    count_converts = count_converts + 1
                    adapted_obj.edtf_date = str(new_expression)
                    obj.reindexObject()

                except EDTFParseException:
                    count_parser_errors = count_parser_errors + 1
                except Exception:
                    count_other_errors = count_other_errors + 1
            except Exception:
                count_other_errors = count_other_errors + 1
        if count_total % 100 == 0:
            logger.info("processed {0} from {1} items ...".format(count_total, len(edtfs)))

    logger.info("total {0} setted edtf_date values from {1} items".format(count_values, len(edtfs)))
    logger.info("Values with no changes: {0}; values succesfully converted: {1}; values with parse errors: {2}; values with some other errors: {2};".format(count_nochanges, count_converts, count_parser_errors, count_other_errors))
    transaction.commit()
