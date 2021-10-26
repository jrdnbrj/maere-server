from graphene import ObjectType
from graphene import List

from ...services.contact_service import get_contacts
from ..type import ContactType


class Query(ObjectType):
    get_contacts = List(ContactType)

    def resolve_get_contacts(parent, info):
        return get_contacts()
