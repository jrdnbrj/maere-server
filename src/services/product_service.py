from decouple import config

from ..db.documents import Product
from .utils import base64_to_file


def get_products():
    products = Product.objects()

    for product in products:
        product.image = config('URL') + 'static/' + product.image

    return products


def create_product(**kwargs):
    img = kwargs.get('image').split('base64,')[1]
    kwargs['image'] = base64_to_file(img)

    Product(**kwargs).save()
    
    return True


def edit_product(**kwargs):
    product = Product.objects(id=kwargs.get('id'))

    if kwargs.get('image') is None:
        kwargs.pop('image')
    else:
        img = kwargs.get('image').split('base64,')[1]
        kwargs['image'] = base64_to_file(img)

    product.update(**kwargs)

    return True


def delete_product(id):
    Product.objects(id=id).delete()

    return True
