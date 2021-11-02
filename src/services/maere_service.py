from ..db.documents import (
    Carousel, 
    Home, 
    ProductHeader, 
    Us, 
    ContactInfo
)

from decouple import config


def create_carousel(**kwargs):
    return Carousel(**kwargs).save()

def get_carousel():
    carousel = Carousel.objects().order_by('sequence')

    for item in carousel:
        item.image = config('URL') + 'static/' + item.image

    return carousel

def edit_carousel(**kwargs):
    carousel = Carousel.objects(id=kwargs.get('id'))
    carousel.update(**kwargs)

    return True

def delete_carousel(id):
    carousel = Carousel.objects(id=id)
    carousel.delete()

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
