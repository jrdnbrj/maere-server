from ..db.documents import Product

from decouple import config


def get_products():
    products = Product.objects()

    for product in products:
        product.image = config('URL') + 'static/' + product.image

    return products

def create_product(**kwargs):
    return Product(**kwargs).save()
