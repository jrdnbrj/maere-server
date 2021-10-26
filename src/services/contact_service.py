from ..db.documents import Contact


def get_contacts():
    return Contact.objects()

def create_contact(**kwargs):
    return Contact(**kwargs).save()

def delete_contact(id):
    try:
        contact = Contact.objects(id=id).first()
        contact.delete()
        return True
    except:
        return False
