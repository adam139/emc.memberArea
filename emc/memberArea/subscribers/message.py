#-*- coding: UTF-8 -*-
from five import grok
from emc.memberArea.interfaces import IMemberAreaCreatedEvent

from Products.CMFCore.utils import getToolByName
from plone.dexterity.utils import createContentInContainer
from Products.PluggableAuthService.interfaces.authservice import IPropertiedUser

from zope.lifecycleevent.interfaces import IObjectAddedEvent

@grok.subscribe(IPropertiedUser,IMemberAreaCreatedEvent)
def create_messagebox(obj,event):
    """创建个人信箱"""
    pm = getToolByName(obj,'portal_membership')
    fd = pm.getHomeFolder(pm.getAuthenticatedMember().getId())
    if fd is None: return    
    id = 'messagebox'
    item = createContentInContainer(fd,"emc.memberArea.messagebox",checkConstraints=False,id=id)
    item.id = id
    item.title = u'个人信箱'
    inputbox = createContentInContainer(item,"emc.memberArea.inputbox",checkConstraints=False,id="inputbox")
    inputbox.title = u"收件箱"
    outputbox = createContentInContainer(item,"emc.memberArea.outputbox",checkConstraints=False,id="outputbox")
    outputbox.title = u"发件箱"

def get_personal_inputbox_byid(id):
    pm = getToolByName(obj,'portal_membership')
    hf = pm.getHomeFolder(id)
    box = hf['messagebox']['inputbox']    
    return box




@grok.subscribe(IMessage,IObjectAddedEvent)
def dispatch_message(obj,event):
    """This handler will deliver message to incoming box of receivers""" 
    receivers = obj.sendto
    from plone import api
    portal = api.portal.get()
    for i in receivers:
        inputbox = get_personal_inputbox_byid(i)
        api.content.copy(source=obj, target=inputbox)
        id = obj.id
        # mark the new obj as unreadet status
        api.content.transition(obj=inputbox[id], transition='undo')
#         message = createContentInContainer(inputbox,"emc.memberArea.message",checkConstraints=False,id=obj.id)
#         message.title = obj.title
#         message.description = obj.description
         

