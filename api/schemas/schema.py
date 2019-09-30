import graphene
from .task_schema import task_schema
from .user_schema import user_schema


class Query(task_schema.TaskQuery, user_schema.UserQuery, graphene.ObjectType):
    pass


class Mutation(task_schema.TaskMutation, user_schema.UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
