import unittest as unittest

from emc.memberArea.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles
#from plone.namedfile.file import NamedImage

class Allcontents(unittest.TestCase):
    layer = INTEGRATION_TESTING
    
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))

        portal.invokeFactory('emc.memberArea.messagebox', 'folder1')
        portal.invokeFactory('emc.memberArea.myfolder', 'my1')
        portal.invokeFactory('emc.memberArea.todo', 'to1',title="todo items")        
        portal['folder1'].invokeFactory('emc.memberArea.inputbox', 'input1')
        portal['folder1'].invokeFactory('emc.memberArea.outputbox', 'output1')
        portal['folder1']['input1'].invokeFactory('emc.memberArea.message', 'message1')
        portal['folder1']['output1'].invokeFactory('emc.memberArea.message', 'message1')          
             

        self.portal = portal
    
    def test_item_types(self):
        self.assertEqual(self.portal['folder1'].id,'folder1')
        self.assertEqual(self.portal['my1'].id,'my1')
        self.assertEqual(self.portal['to1'].id,'to1')
        import pdb
        pdb.set_trace()        
        self.assertEqual(self.portal['folder1']['input1'].id,'input1') 
        self.assertEqual(self.portal['folder1']['output1'].id,'output1')                
        self.assertEqual(self.portal['folder1']['input1']['message1'].id,'message1') 
        self.assertEqual(self.portal['folder1']['output1']['message1'].id,'message1') 
        
    def test_interface(self):
        from emc.memberArea.content.messagebox import IMessagebox
        from emc.memberArea.content.message import IMessage        
        from emc.memberArea.content.inputbox import IInputbox
        from emc.memberArea.content.outputbox import IOutputbox
        from emc.memberArea.content.myfolder import IMyfolder
        from emc.memberArea.content.todo import ITodo                        
        self.assertTrue(IMessagebox.providedBy(self.portal['folder1']['input1']))
        self.assertTrue(IInputbox.providedBy(self.portal['folder1']['input1']))
        self.assertFalse(IMessagebox.implementedBy(self.portal['folder1']['input1']))                
        self.assertTrue(IMessagebox.providedBy(self.portal['folder1']['output1']))
        self.assertTrue(IOutputbox.providedBy(self.portal['folder1']['output1']))        
        self.assertTrue(IMessage.providedBy(self.portal['folder1']['output1']['message1']))
        self.assertTrue(IMyfolder.providedBy(self.portal['my1']))
        self.assertTrue(ITodo.providedBy(self.portal['to1']))                                         
                  
       
        