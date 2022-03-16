from graphene import ObjectType
from graphene import List, Boolean

from ...services.contact_service import get_contacts
from ...middleware import authentication_required
from ..type import ContactType
from ...services.utils import send_email

class Query(ObjectType):
    get_contacts = List(ContactType)
    # send_email = Boolean()

    @authentication_required()
    def resolve_get_contacts(parent, info):
        return get_contacts()

    # def resolve_send_email(parent, info):
    #     return send_email()
