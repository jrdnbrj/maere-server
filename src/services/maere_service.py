from decouple import config

from ..db.documents import (
    Carousel, 
    Home, 
    ProductHeader, 
    Us, 
    ContactInfo,
    Address
)
from .utils import (
    base64_to_file, 
    generate_token, 
    verify_password, 
    encrypt_password
)

def create_carousel(**kwargs):
    img = kwargs.get('image').split('base64,')[1]
    kwargs['image'] = base64_to_file(img)
    
    Carousel(**kwargs).save()

    return True

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

def get_address():
    return Address.objects().first().address

def edit_address(**kwargs):
    address = Address.objects().first()
    address.update(**kwargs)

    return True

def login(password):
    success, _ = verify_password(password)

    if success:
        return generate_token(), True

    return 'La contraseña es incorrecta.', False

def update_password(password, new_password):
    success, session = verify_password(password)

    if success:
        if len(new_password) < 8:
            return 'La nueva contraseña debe tener al menos 8 caracteres.'

        if len(new_password) > 20:
            return 'La nueva contraseña debe tener menos de 20 caracteres.'

        session.password = encrypt_password(new_password)
        session.save()
        
        return 'OK'
    else:
        return 'La contraseña actual es incorrecta.'
