from mongoengine.document import Document
from mongoengine.fields import StringField, IntField


class Category(Document):
    name = StringField(required=True, unique=True)
    sequence = IntField(required=True)

class Product(Document):
    name = StringField(required=True)
    formulator = StringField(required=True)
    category = StringField(required=True)
    image = StringField()

class Contact(Document):
    name = StringField()
    phone = StringField()
    email = StringField()
    message = StringField()
