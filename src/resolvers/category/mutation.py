from graphene import ObjectType, Mutation
from graphene import String, Boolean

from ...services.category_service import create_category


class CreateCategory(Mutation):
    class Arguments:
        name = String(required=True)

    result = Boolean()

    def mutate(root, info, name=None):
        result = create_category(name=name)
        return { 'result': result }


class Mutation(ObjectType):
    create_category = CreateCategory.Field()
