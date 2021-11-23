from graphene import ObjectType, Mutation, String, Boolean

from ...middleware import authentication_required
from ...services.category_service import (
    create_category, 
    edit_category, 
    delete_category
)

class CreateCategory(Mutation):
    class Arguments:
        name = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, name):
        result = create_category(name=name)
        return { 'result': result }

class EditCategory(Mutation):
    class Arguments:
        id = String(required=True)
        name = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id, name):
        result = edit_category(id=id, name=name)
        return { 'result': result }

class DeleteCategory(Mutation):
    class Arguments:
        id = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id):
        result = delete_category(id=id)
        return { 'result': result }

class Mutation(ObjectType):
    create_category = CreateCategory.Field()
    edit_category = EditCategory.Field()
    delete_category = DeleteCategory.Field()
