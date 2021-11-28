from mongoengine.document import Document
from mongoengine.fields import (
    StringField, 
    IntField, 
    DateTimeField,
    URLField
)

from datetime import datetime


class Category(Document):
    name = StringField(required=True, unique=True)
    sequence = IntField(required=True, unique=True)

class Product(Document):
    name = StringField(required=True)
    formulator = StringField(required=True, min_length=1)
    category = StringField(required=True, min_length=1)
    image = StringField()
    url = URLField()

class Contact(Document):
    name = StringField()
    phone = StringField()
    email = StringField()
    message = StringField()
    created_at = DateTimeField(default=datetime.utcnow)

class Carousel(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    image = StringField(required=True)
    sequence = IntField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class Home(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class ProductHeader(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class Us(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    sequence = IntField(required=True, unique=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class ContactInfo(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    sequence = IntField(required=True, unique=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class Password(Document):
    password = StringField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)

class Address(Document):
    address = StringField(required=True)
    updated_at = DateTimeField(default=datetime.utcnow)
