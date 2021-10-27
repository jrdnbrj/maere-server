from graphene import ObjectType, List, Field

from ...services.maere_service import (
    get_carousel, 
    get_home, 
    get_product_header, 
    get_us, 
    get_contact_info
)
from ..type import (
    CarouselType, 
    HomeType, 
    ProductHeaderType, 
    UsType, 
    ContactInfoType
)


class Query(ObjectType):
    get_carousel = List(CarouselType)
    get_home = Field(HomeType)
    get_product_header = Field(ProductHeaderType)
    get_us = List(UsType)
    get_contact_info = List(ContactInfoType)

    def resolve_get_carousel(parent, info):
        return get_carousel()
    
    def resolve_get_home(parent, info):
        return get_home()

    def resolve_get_product_header(parent, info):
        return get_product_header()

    def resolve_get_us(parent, info):
        return get_us()

    def resolve_get_contact_info(parent, info):
        return get_contact_info()

