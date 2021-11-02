from ..db.documents import Contact


def get_contacts():
    return Contact.objects()

def create_contact(**kwargs):
    Contact(**kwargs).save()

    return True

def delete_contact(id):
    contact = Contact.objects(id=id).first()
    contact.delete()

    return True
