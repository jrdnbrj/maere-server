from ..db.documents import (
    Carousel, 
    Home, 
    ProductHeader, 
    Us, 
    ContactInfo
)

from decouple import config


def get_carousel():
    carousel = Carousel.objects().order_by('sequence')

    for item in carousel:
        item.image = config('URL') + 'static/' + item.image

    return carousel

def create_carousel(**kwargs):
    return Carousel(**kwargs).save()

def get_home():
    return Home.objects().first()

def get_product_header():
    return ProductHeader.objects().first()

def get_us():
    return Us.objects().order_by('sequence')

def get_contact_info():
    return ContactInfo.objects().order_by('sequence')
