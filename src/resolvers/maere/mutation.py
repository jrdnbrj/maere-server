from graphene import ObjectType, Mutation
from graphene import String

from ...services.maere_service import create_carousel


class CreateCarousel(Mutation):
    class Arguments:
        title = String()
        text = String()
        image = String()
        sequence = String()

    id = String()
    title = String()
    text = String()
    image = String()
    sequence = String()

    def mutate(root, info, title=None, text=None, image=None, sequence=None):
        return create_carousel(title=title, text=text, image=image, sequence=sequence)


class Mutation(ObjectType):
    create_carousel = CreateCarousel.Field()
