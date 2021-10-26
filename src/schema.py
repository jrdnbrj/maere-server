from graphene import ObjectType, Schema

from .resolvers.product.query import Query as product_query
from .resolvers.category.query import Query as category_query
from .resolvers.contact.query import Query as contact_query

from .resolvers.product.mutation import Mutation as product_mutation
from .resolvers.category.mutation import Mutation as category_mutation
from .resolvers.contact.mutation import Mutation as contact_mutation

class Query(product_query, category_query, contact_query, ObjectType):
    pass

class Mutation(product_mutation, category_mutation, contact_mutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)
