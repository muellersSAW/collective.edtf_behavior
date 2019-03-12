# -*- coding: utf-8 -*-
from collective.edtf_behavior.behaviors.e_d_t_f_date import IEDTFDateMarker
from collective.edtf_behavior.testing import COLLECTIVE_EDTF_BEHAVIOR_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class EDTFDateIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_EDTF_BEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_e_d_t_f_date(self):
        behavior = getUtility(IBehavior, 'collective.edtf_behavior.e_d_t_f_date')
        self.assertEqual(
            behavior.marker,
            IEDTFDateMarker,
        )
