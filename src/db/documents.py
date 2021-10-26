from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, DateTimeField

from datetime import datetime


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
    created_at = DateTimeField(default=datetime.utcnow)

class Carousel(Document):
    title = StringField()
    text = StringField()
    image = StringField()
    sequence = IntField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class Home(Document):
    title = StringField()
    text = StringField()
    updated_at = DateTimeField(default=datetime.utcnow)

class ProductHeader(Document):
    title = StringField()
    text = StringField()
    updated_at = DateTimeField(default=datetime.utcnow)

class Us(Document):
    title = StringField()
    text = StringField()
    sequence = IntField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class ContactInfo(Document):
    title = StringField()
    text = StringField()
    sequence = IntField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)
