from graphene import ObjectType, Schema

from .resolvers.product.query import Query as product_query
from .resolvers.category.query import Query as category_query

from .resolvers.product.mutation import Mutation as product_mutation
from .resolvers.category.mutation import Mutation as category_mutation

class Query(product_query, category_query, ObjectType):
    pass

class Mutation(product_mutation, category_mutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)
