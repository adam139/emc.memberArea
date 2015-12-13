#-*- coding: UTF-8 -*-
from five import grok
from emc.memberArea.interfaces import IMemberAreaCreatedEvent

from Products.CMFCore.utils import getToolByName
from plone.dexterity.utils import createContentInContainer
from Products.PluggableAuthService.interfaces.authservice import IPropertiedUser

from zope.lifecycleevent.interfaces import IObjectAddedEvent

@grok.subscribe(IPropertiedUser,IMemberAreaCreatedEvent)
def creatementionwofolder(obj,event):
    """创建提到我文件夹"""
    pm = getToolByName(obj,'portal_membership')
    fd = pm.getHomeFolder(pm.getAuthenticatedMember().getId())
    if fd is None: return    
    id = 'messagebox'
    item = createContentInContainer(file,"emc.memberArea.messagebox",checkConstraints=False,id=id)
    item.id = id
    item.title = u'个人信箱'


  

