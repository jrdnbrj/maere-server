from graphene import ObjectType, String, Int, DateTime


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

class ContactType(ObjectType):
    id = String()
    name = String()
    phone = String()
    email = String()
    message = String()
    created_at = DateTime()
