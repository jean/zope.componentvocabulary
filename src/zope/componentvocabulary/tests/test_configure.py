##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import unittest
import zope.component
import zope.configuration.xmlconfig


class ZCMLTest(unittest.TestCase):

    def test_configure_zcml_should_be_loadable(self):
        try:
            zope.configuration.xmlconfig.XMLConfig(
                'configure.zcml', zope.componentvocabulary)()
        except Exception, e:
            self.fail(e)

    def test_configure_should_register_n_utilities(self):
        gsm = zope.component.getGlobalSiteManager()
        count = len(list(gsm.registeredUtilities()))
        zope.configuration.xmlconfig.XMLConfig(
            'configure.zcml', zope.componentvocabulary)()
        self.assertEqual(count + 11, len(list(gsm.registeredUtilities())))
