from graphene import ObjectType, Mutation
from graphene import String, Boolean

from ...services.product_service import (
    create_product, 
    edit_product, 
    delete_product
)

class CreateProduct(Mutation):
    class Arguments:
        name = String(required=True)
        formulator = String(required=True)
        category = String(required=True)
        url = String(required=True)
        image = String(required=True)

    result = Boolean()

    def mutate(root, info, name, formulator, category, url, image):
        result = create_product(
            name=name, 
            formulator=formulator,
            category=category,
            url=url,
            image=image
        )
        return { 'result': result }

class EditProduct(Mutation):
    class Arguments:
        id = String(required=True)
        name = String(required=True)
        formulator = String(required=True)
        category = String(required=True)
        url = String(required=True)
        image = String()

    result = Boolean()

    def mutate(root, info, id, name, formulator, category, url, image=None):
        result = edit_product(
            id=id, 
            name=name, 
            formulator=formulator,
            category=category,
            url=url,
            image=image
        )
        return { 'result': result }

class DeleteProduct(Mutation):
    class Arguments:
        id = String(required=True)

    result = Boolean()

    def mutate(root, info, id):
        result = delete_product(id=id)
        return { 'result': result }

class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    edit_product = EditProduct.Field()
    delete_product = DeleteProduct.Field()
