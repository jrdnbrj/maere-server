import os
from decouple import config

from ..db.documents import (
    Carousel, 
    Home, 
    ProductHeader, 
    Us, 
    ContactInfo
)
from .utils import base64_to_file


def create_carousel(**kwargs):
    img = kwargs.get('image').split('base64,')[1]
    kwargs['image'] = base64_to_file(img)

    return Carousel(**kwargs).save()

def get_carousel():
    carousel = Carousel.objects().order_by('sequence')

    for item in carousel:
        item.image = config('URL') + 'static/' + item.image

    return carousel

def edit_carousel(**kwargs):
    carousel = Carousel.objects(id=kwargs.get('id'))

    if kwargs.get('image') is None:
        kwargs.pop('image')
    else:
        img = kwargs.get('image').split('base64,')[1]
        kwargs['image'] = base64_to_file(img)

    carousel.update(**kwargs)

    return True

def delete_carousel(id):
    Carousel.objects(id=id).delete()
    
    return True

def get_home():
    return Home.objects().first()

def edit_home(**kwargs):
    home = Home.objects().first()
    home.update(**kwargs)

    return True

def get_product_header():
    return ProductHeader.objects().first()

def edit_product_header(**kwargs):
    product_header = ProductHeader.objects().first()
    product_header.update(**kwargs)

    return True

def get_us():
    return Us.objects().order_by('sequence')

def edit_us(**kwargs):
    us = Us.objects(id=kwargs.get('id'))
    us.update(**kwargs)

    return True

def get_contact_info():
    return ContactInfo.objects().order_by('sequence')

def edit_contact_info(**kwargs):
    contact_info = ContactInfo.objects(id=kwargs.get('id'))
    contact_info.update(**kwargs)

    return True
