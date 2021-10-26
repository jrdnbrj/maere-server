from graphene import ObjectType, String


class ProductType(ObjectType):
    id = String()
    name = String()
    formulator = String()
    category = String()
    image = String()
