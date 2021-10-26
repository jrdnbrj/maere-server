from ..db.documents import (
    Carousel, 
    Home, 
    ProductHeader, 
    Us, 
    ContactInfo
)


def get_carousel():
    return Carousel.objects().order_by('sequence')

def create_carousel(**kwargs):
    return Carousel(**kwargs).save()

def get_home():
    return Home.objects()

def get_product_header():
    return ProductHeader.objects()

def get_us():
    return Us.objects()

def get_contact_info():
    return ContactInfo.objects()
