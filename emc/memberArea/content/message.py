#-*- coding: UTF-8 -*-
from five import grok
from zope import schema
from plone.directives import form, dexterity
from plone.app.dexterity.behaviors.metadata import IBasic

from collective import dexteritytextindexer
from collective.dexteritytextindexer.behavior import IDexterityTextIndexer

from emc.memberArea import _

class IMessage(form.Schema,IBasic):
    """
    emc project member area message content type
    """
#标准名称
    dexteritytextindexer.searchable('title')    
    title = schema.TextLine(title=_(u"standard name"),
                             default=u"",
                            required=True,) 
#标准描述        
    description = schema.TextLine(title=_(u"standard description"),
                             default=u"",
                             required=False,)        


 
