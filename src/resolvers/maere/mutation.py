from graphene import ObjectType, Mutation, String, Boolean

from ...services.maere_service import (
    create_carousel,
    edit_carousel,
    edit_home,
    edit_product_header,
    edit_us,
    edit_contact_info
)


class CreateCarousel(Mutation):
    class Arguments:
        title = String()
        text = String()
        image = String()
        sequence = String()

    result = Boolean()

    def mutate(root, info, title=None, text=None, image=None, sequence=None):
        result = create_carousel(
            title=title, 
            text=text, 
            image=image, 
            sequence=sequence
        )
        return { 'result': result }

class EditCarousel(Mutation):
    class Arguments:
        id = String()
        title = String()
        text = String()
        image = String()
        sequence = String()

    result = Boolean()

    def mutate(root, info, id=None, title=None, text=None, image=None, sequence=None):
        result = edit_carousel(
            id=id, 
            title=title, 
            text=text, 
            image=image, 
            sequence=sequence
        )
        return { 'result': result }

class DeleteCarousel(Mutation):
    class Arguments:
        id = String()

    result = Boolean()

    def mutate(root, info, id=None):
        result = edit_carousel(id=id)
        return { 'result': result }

class EditHome(Mutation):
    class Arguments:
        title = String()
        text = String()

    result = Boolean()

    def mutate(root, info, title=None, text=None):
        result = edit_home(title=title, text=text)
        return { 'result': result }

class EditProductHeader(Mutation):
    class Arguments:
        title = String()
        text = String()

    result = Boolean()

    def mutate(root, info, title=None, text=None):
        result = edit_product_header(title=title, text=text)
        return { 'result': result }

class EditUs(Mutation):
    class Arguments:
        id = String()
        title = String()
        text = String()

    result = Boolean()

    def mutate(root, info, id=None, title=None, text=None):
        result = edit_us(id=id, title=title, text=text)
        return { 'result': result }

class EditContactInfo(Mutation):
    class Arguments:
        id = String()
        title = String()
        text = String()

    result = Boolean()

    def mutate(root, info, id=None, title=None, text=None):
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
