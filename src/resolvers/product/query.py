from graphene import ObjectType
from graphene import List

from ...services.product_service import get_products
from ..type import ProductType


class Query(ObjectType):
    get_products = List(ProductType)

    def resolve_get_products(parent, info):
        return get_products()

