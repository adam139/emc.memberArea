#-*- coding: UTF-8 -*-
from five import grok
from zope import schema
from zope.interface import Interface
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
import datetime

from z3c.form.form import extends
from z3c.form import field

from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity
from plone.app.dexterity.behaviors.metadata import IBasic
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from collective import dexteritytextindexer



#from example.conference.presenter import IPresenter

#from collective.dexteritytextindexer.behavior import IDexterityTextIndexer
#from emc.bokeh.registrysource import DynamicVocabulary
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
   
        

#包含图像数据的csv文件   
    upload = NamedBlobFile(title=_(u"figure data"),
        description=_(u"Attach your figure data report file(csv format)."),
        required=False,
    )
 
