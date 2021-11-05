from graphene import ObjectType, Mutation, String, Boolean, Int, ID

from ...services.maere_service import (
    create_carousel,
    edit_carousel,
    delete_carousel,
    edit_home,
    edit_product_header,
    edit_us,
    edit_contact_info
)


class CreateCarousel(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)
        image = String(required=True)
        sequence = Int(required=True)

    result = Boolean()

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

    def mutate(root, info, id):
        result = delete_carousel(id=id)
        return { 'result': result }

class EditHome(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    def mutate(root, info, title, text):
        result = edit_home(title=title, text=text)
        return { 'result': result }

class EditProductHeader(Mutation):
    class Arguments:
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    def mutate(root, info, title, text):
        result = edit_product_header(title=title, text=text)
        return { 'result': result }

class EditUs(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    def mutate(root, info, id, title, text):
        result = edit_us(id=id, title=title, text=text)
        return { 'result': result }

class EditContactInfo(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String(required=True)
        text = String(required=True)

    result = Boolean()

    def mutate(root, info, id, title, text):
        result = edit_contact_info(id=id, title=title, text=text)
        return { 'result': result }

class Mutation(ObjectType):
    create_carousel = CreateCarousel.Field()
    edit_carousel = EditCarousel.Field()
    delete_carousel = DeleteCarousel.Field()
    edit_home = EditHome.Field()
    edit_product_header = EditProductHeader.Field()
    edit_us = EditUs.Field()
    edit_contact_info = EditContactInfo.Field()
