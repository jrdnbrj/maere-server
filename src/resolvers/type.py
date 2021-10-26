from graphene import ObjectType, String, Int


class ProductType(ObjectType):
    id = String()
    name = String()
    formulator = String()
    category = String()
    image = String()

class CategoryType(ObjectType):
    id = String()
    name = String()
    sequence = Int()
