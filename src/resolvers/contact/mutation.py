from graphene import ObjectType, Mutation, String, Boolean

from ...services.contact_service import create_contact, delete_contact


class CreateContact(Mutation):
    class Arguments:
        name = String()
        phone = String()
        email = String()
        message = String()

    id = String()
    name = String()
    phone = String()
    email = String()
    message = String()

    def mutate(root, info, name=None, phone=None, email=None, message=None):
        result = create_contact(
            name=name, 
            phone=phone, 
            email=email, 
            message=message
        )
        return { 'result': result }


class DeleteContact(Mutation):
    class Arguments:
        id = String(required=True)

    result = Boolean()

    def mutate(root, info, id=None):
        result = delete_contact(id)
        return { 'result': result }


class Mutation(ObjectType):
    create_contact = CreateContact.Field()
    delete_contact = DeleteContact.Field()
