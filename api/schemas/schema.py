import graphene
from .task_schema import task_schema


class Query(task_schema.TaskQuery):
    pass


class Mutation(task_schema.TaskMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
