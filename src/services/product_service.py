from datetime import datetime
import base64

from decouple import config
from ..db.documents import Product


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

    if '/static/' not in kwargs.get('image'):
        img = kwargs.get('image').split('base64,')[1]
        kwargs['image'] = base64_to_file(img)
    else:
        kwargs['image'] = kwargs.get('image').split('/')[-1]

    product.update(**kwargs)

    return True


def delete_product(id):
    Product.objects(id=id).delete()

    return True


def base64_to_file(img_encoded):
    img = base64.b64decode(img_encoded)
    filename = str(datetime.now()) + '.jpg'

    with open('static/' + filename, 'wb') as file:
        file.write(img)
    
    return filename
