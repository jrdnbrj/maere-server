from graphene import ObjectType
from graphene import List

from ...services.category_service import get_categories
from ..type import CategoryType


class Query(ObjectType):
    get_categories = List(CategoryType)

    def resolve_get_categories(parent, info):
        return get_categories()

