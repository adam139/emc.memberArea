from zope import interface
from zope.component.interfaces import ObjectEvent
from emc.memberArea.interfaces import IMemberAreaCreatedEvent
from emc.memberArea.interfaces import IAddFavoriteEvent
from emc.memberArea.interfaces import ISendMessageEvent

class MemberAreaCreatedEvent(ObjectEvent):
    interface.implements(IMemberAreaCreatedEvent)

class AddFavoriteEvent(ObjectEvent):
    interface.implements(IAddFavoriteEvent)

class SendMessageEvent(ObjectEvent):
    interface.implements(ISendMessageEvent)
           