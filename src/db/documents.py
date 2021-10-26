from mongoengine.document import Document
from mongoengine.fields import StringField, EnumField

from enum import Enum


class Formulator(Enum):
    Catawba = 'Catawba Enterprising'
    Symborg = 'Symborg'
    Folterra = 'Folterra'
    ACP = 'Agrocorrectores del Pacífico'

class Category(Enum):
    Bioestimulante = 'Bioestimulante'
    Biopesticida = 'Biopesticida'
    Biofertilizante = 'Biofertilizante'
    Corrector = 'Corrector de Suelo'
    Fertilizante = 'Fertilizante Foliar'

class Product(Document):
    name = StringField(required=True)
    formulator = EnumField(Formulator, required=True)
    category = EnumField(Category, required=True)
    image = StringField()

class Contact(Document):
    name = StringField()
    phone = StringField()
    email = StringField()
    message = StringField()
