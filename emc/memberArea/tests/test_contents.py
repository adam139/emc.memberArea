import unittest as unittest

from emc.memberArea.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles
#from plone.namedfile.file import NamedImage

class Allcontents(unittest.TestCase):
    layer = INTEGRATION_TESTING
    
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))

        portal.invokeFactory('emc.memberArea.messagebox', 'messagebox1')
        portal['messagebox1'].invokeFactory('emc.memberArea.message', 'message1')        

        self.portal = portal
    
    def test_item_types(self):
        self.assertEqual(self.portal['messagebox1'].id,'messagebox1')
        self.assertEqual(self.portal['messagebox1']['message1'].id,'message1')    
        