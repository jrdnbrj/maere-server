from graphene import ObjectType, Mutation, String, Boolean, Int, ID

from ...middleware import authentication_required
from ...services.maere_service import (
    create_carousel,
    edit_carousel,
    delete_carousel,
    edit_home,
    edit_product_header,
    edit_us,
    edit_contact_info,
    edit_address,
    login,
    update_password
)


class CreateCarousel(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)
        image = String(required=True)
        sequence = Int(required=True)

    result = Boolean()

    # @authentication_required()
    def mutate(root, info, title, text, image, sequence):
        result = create_carousel(
            title=title, 
            text=text, 
            image=image, 
            sequence=sequence
        )
        return { 'result': result }

class EditCarousel(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String(required=True)
        text = String(required=True)
        sequence = Int(required=True)
        image = String()

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id, title, text, sequence, image=None):
        result = edit_carousel(
            id=id, 
            title=title, 
            text=text, 
            sequence=sequence,
            image=image
        )
        return { 'result': result }

class DeleteCarousel(Mutation):
    class Arguments:
        id = ID(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id):
        result = delete_carousel(id=id)
        return { 'result': result }

class EditHome(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, title, text):
        result = edit_home(title=title, text=text)
        return { 'result': result }

class EditProductHeader(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, title, text):
        result = edit_product_header(title=title, text=text)
        return { 'result': result }

class EditUs(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id, title, text):
        result = edit_us(id=id, title=title, text=text)
        return { 'result': result }

class EditContactInfo(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    @authentication_required()
    def mutate(root, info, id, title, text):
        result = edit_contact_info(id=id, title=title, text=text)
        return { 'result': result }

class Login(Mutation):
    class Arguments:
        password = String(required=True)
    
    token = String()
    success = Boolean()

    def mutate(self, info, password):
        token, success = login(password)
        return {'token': token, 'success': success}

class EditAddress(Mutation):
    class Arguments:
        address = String(required=True)

    result = Boolean()

    # @authentication_required()
    def mutate(root, info, address):
        result = edit_address(address=address)
        return { 'result': result }

class UpdatePassword(Mutation):
    class Arguments:
        password = String(required=True)
        new_password = String(required=True)

    response = String()

    # @authentication_required()
    def mutate(root, info, password=None, new_password=None):
        response = update_password(password, new_password)
        return { 'response': response }

class Mutation(ObjectType):
    create_carousel = CreateCarousel.Field()
    edit_carousel = EditCarousel.Field()
    delete_carousel = DeleteCarousel.Field()
    edit_home = EditHome.Field()
    edit_product_header = EditProductHeader.Field()
    edit_us = EditUs.Field()
    edit_contact_info = EditContactInfo.Field()
    edit_address = EditAddress.Field()
    login = Login.Field()
    update_password = UpdatePassword.Field()
