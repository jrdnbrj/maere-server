from graphene import ObjectType, Mutation
from graphene import String, Boolean

from ...services.product_service import create_product


class CreateProduct(Mutation):
    class Arguments:
        name = String(required=True)
        formulator = String(required=True)
        category = String(required=True)

    result = Boolean()

    def mutate(root, info, name=None, formulator=None, category=None):
        result = create_product(
            name=name, 
            formulator=formulator,
            category=category
        )
        return { 'result': result }


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
