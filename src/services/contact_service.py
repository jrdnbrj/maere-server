from ..db.documents import Contact

from .utils import send_email


def get_contacts():
    return Contact.objects()

def create_contact(**kwargs):
    send_email(kwargs)
    Contact(**kwargs).save()

    return True

def delete_contact(id):
    contact = Contact.objects(id=id).first()
    contact.delete()

    return True
