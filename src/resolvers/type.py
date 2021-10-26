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

class CarouselType(ObjectType):
    title = String()
    text = String()
    image = String()
    sequence = Int()
    updated_at = DateTime()

class HomeType(ObjectType):
    title = String()
    text = String()
    updated_at = DateTime()

class ProductHeaderType(ObjectType):
    title = String()
    text = String()
    updated_at = DateTime()

class UsType(ObjectType):
    title = String()
    text = String()
    sequence = Int()
    updated_at = DateTime()

class ContactInfoType(ObjectType):
    title = String()
    text = String()
    sequence = Int()
    updated_at = DateTime()